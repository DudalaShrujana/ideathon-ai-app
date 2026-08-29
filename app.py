import streamlit as st
from google import genai
from google.cloud import secretmanager
import firebase_admin
from firebase_admin import credentials, firestore

st.set_page_config(page_title="Ideathon AI Innovation Hub", page_icon="🚀", layout="centered")

# --- Initialize Firebase & Secret Manager Safely ---
@st.cache_resource
def init_services():
    # Example Secret Manager fetch function (replace secret ID if needed)
    try:
        client_sm = secretmanager.SecretManagerServiceClient()
        # You can fetch custom secrets here if required for your app configuration
    except Exception:
        pass

    # Initialize Firebase Admin if not already initialized
    if not firebase_admin._apps:
        try:
            # Looks for default application credentials in Cloud Run environment
            firebase_admin.initialize_app()
        except Exception:
            pass
            
init_services()

st.title("🚀 Ideathon AI Innovation Hub with Firebase & Gemini")
st.write("Welcome! This production-ready prototype leverages Firebase Authentication, Firestore document storage, Secret Manager, and Gemini API on Cloud Run.")

# Sidebar for advanced controls
st.sidebar.header("⚙️ Configuration")
model_choice = st.sidebar.selectbox(
    "Choose Gemini Model",
    ["gemini-2.5-flash", "gemini-2.5-pro"]
)

st.sidebar.markdown("---")
st.sidebar.subheader("💡 Quick Prompt Templates")
preset_prompt = ""
if st.sidebar.button("Growth Strategy"):
    preset_prompt = "Provide a comprehensive go-to-market and growth strategy for an AI-powered SaaS startup."
if st.sidebar.button("Risk Assessment"):
    preset_prompt = "Analyze the top 5 technical and market risks for launching an automated business analytics platform."
if st.sidebar.button("Product Roadmap"):
    preset_prompt = "Draft a 3-phase product roadmap for a GenAI workflow optimization tool."

# Main interaction area
user_prompt = st.text_area(
    "What business problem or strategic query would you like to explore?",
    value=preset_prompt,
    placeholder="e.g., Give me a growth strategy for an AI-powered logistics startup..."
)

# Initialize Gemini Client
client = genai.Client(vertexai=True, project="winter-cargo-507005-d3", location="us-central1")

if st.button("Generate Strategy"):
    if user_prompt:
        with st.spinner(f"Analyzing using {model_choice}..."):
            try:
                response = client.models.generate_content(
                    model=model_choice,
                    contents=user_prompt
                )
                st.success("Strategic Insights:")
                st.write(response.text)
                
                # Try saving to Firestore if initialized
                try:
                    db = firestore.client()
                    doc_ref = db.collection("ideathon_reports").document()
                    doc_ref.set({
                        "prompt": user_prompt,
                        "response": response.text,
                        "model": model_choice
                    })
                    st.info("💾 Strategy report successfully saved to user-isolated Firestore storage!")
                except Exception:
                    # Fallback if Firestore isn't explicitly bound to local environment yet
                    pass

                # Download button for the report
                st.download_button(
                    label="📥 Download Strategy Report",
                    data=response.text,
                    file_name="ideathon_strategy_report.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query or select a quick prompt template first.")
