from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from google import genai

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "online", "message": "Ideathon AI App is running successfully!"}


# Initialize the Gemini Client safely using environment variable
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

class ContentRequest(BaseModel):
    document_id: str
    generated_content: str

@app.post("/api/run-ethics-audit")
def run_ethics_audit(request: ContentRequest):
    prompt = f"""
    Perform an ethics and bias audit on the following text. Evaluate against 4 pillars:
    1. Fairness (score 0-100)
    2. Transparency (score 0-100)
    3. Accountability (score 0-100)
    4. Socioeconomic Impact (score 0-100)
    
    Calculate an overall_score (average of the 4).
    Provide 3 actionable recommendations to mitigate risks.
    
    Return strict JSON with keys: fairness_score, transparency_score, accountability_score, socioeconomic_score, overall_score, recommendations.
    
    Text to audit: "{request.generated_content}"
    """
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
        )
        return {"status": "success", "audit": response.text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/verify-facts")
def verify_facts(request: ContentRequest):
    prompt = f"""
    Analyze the following text for factual claims, potential hallucinations, or unsupported assertions.
    Return a strict JSON object with:
    - credibility_index (integer from 0 to 100)
    - unsupported_claims (list of strings identifying suspicious or unverified statements)
    - citation_suggestions (list of strings on how to substantiate the claims)
    
    Text to analyze: "{request.generated_content}"
    """
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
        )
        return {"status": "success", "fact_check": response.text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/redact-pii")
def redact_pii(request: ContentRequest):
    prompt = f"""
    Scan the following text for any Personally Identifiable Information (PII) such as names, phone numbers, email addresses, physical addresses, or financial IDs.
    Return a strict JSON object with:
    - pii_detected (boolean)
    - redacted_text (the text with sensitive PII masked out using tags like [REDACTED_EMAIL], [REDACTED_NAME], etc.)
    - entities_found (list of strings showing what types of PII were caught)
    
    Text to scan: "{request.generated_content}"
    """
    try:
        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=prompt,
        )
        return {"status": "success", "privacy_shield": response.text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))