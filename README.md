# 🚀 Ideathon AI Innovation Hub

[![Cloud Run Deployment](https://img.shields.io/badge/Google%20Cloud-Cloud%20Run-blue?logo=googlecloud&logoColor=white)](https://ideathon-ai-app-346455634981.us-central1.run.app)
[![Streamlit App](https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Gemini API](https://img.shields.io/badge/AI%20Engine-Vertex%20AI%20%2F%20Gemini-4285F4?logo=google&logoColor=white)](https://cloud.google.com/vertex-ai)
[![Firebase & Firestore](https://img.shields.io/badge/Backend-Firebase%20%2F%20Firestore-FFCA28?logo=firebase&logoColor=black)](https://firebase.google.com)

An enterprise-grade, serverless AI application designed for rapid business ideation, strategic risk assessment, and roadmap planning. Built with **Streamlit**, **Google Cloud Run**, **Firebase**, **Google Cloud Secret Manager**, and powered by multi-turn **Gemini models** via Vertex AI.

---

## 🏗️ Architecture & Technical Stack
[ Streamlit UI (Cloud Run) ]
│

├──► Google GenAI SDK (Vertex AI)

|──► Gemini 2.5 Flash / Pro

├──► Firebase Admin Auth & Firestore 

─► User Session & Data Isolation

└──► Google Cloud Secret Manager 

────► Secure Config Management                                                                                                                                                                                                            
* **Frontend & Presentation:** Streamlit (Python containerized via Docker)
* **AI & Machine Learning Engine:** Google GenAI SDK targeting Vertex AI (`gemini-2.5-flash` & `gemini-2.5-pro`)
* **Backend & Persistence:** Firebase Admin SDK & Cloud Firestore (User-isolated document storage)
* **Security & Configuration:** Google Cloud Secret Manager
* **Infrastructure & Compute:** Serverless Google Cloud Run (`us-central1`)

---

## ✨ Key Features

1. **Multi-Turn Gemini Integration:** Leverages cutting-edge Google Gemini models for deep, context-aware business reasoning, strategy formulation, and dynamic follow-ups.
2. **Dual-Model Selection:** Switch seamlessly between **Gemini 2.5 Flash** (optimized for ultra-low latency response times) and **Gemini 2.5 Pro** (optimized for complex logical reasoning and comprehensive analysis).
3. **Enterprise Security & Isolation:** Integrated with Firebase Auth foundations and server-side Firestore document isolation to store structured prompt-response histories securely.
4. **Secret Manager Pattern:** Implements secure secret fetching pipelines compliant with enterprise-grade GCP standards.
5. **Productivity Tooling:** One-click business prompt templates (*Growth Strategy*, *Risk Assessment*, *Product Roadmap*) and structured report exporting (`.txt`).

---

## 🚀 Live Demo & Access

Experience the live deployed production application:
👉 **[Launch Ideathon AI Innovation Hub](https://ideathon-ai-app-346455634981.us-central1.run.app)**

---

## 🛠️ Local Development & Deployment

### Prerequisites
* Python 3.9+
* Google Cloud SDK (`gcloud`) authenticated to your GCP Project.

### 1. Clone the Repository
```bash
git clone [https://github.com/DudalaShrujana/ideathon-ai-app.git](https://github.com/DudalaShrujana/ideathon-ai-app.git)
cd ideathon-ai-app
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Run Locally
Bash
streamlit run app.py
4. Deploy to Google Cloud Run
Bash
gcloud run deploy ideathon-ai-app \
    --source . \
    --region us-central1 \
    --allow-unauthenticated
