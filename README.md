# CV-Scout
A full AI CV-matching pipeline that analyzes job descriptions and resumes, produces section-level scoring, and delivers detailed reasoning through a clean Streamlit UI.

## 📌 Overview

This project helps HR teams or recruiters **quickly identify top candidates** by comparing CVs to job descriptions.

Key features:

- Section-level scoring: **Skills, Experience, Education, Projects**  
- Hierarchical bullet-point explanations with **ticks (✅)** and **crosses (❌)**  
- Highlights missing **MUST-HAVE requirements**  
- Provides numeric scores (0–100) for each section and overall  
- Ranked candidate list for easy comparison  
- Supports **multiple CV uploads** (up to 100)  
- **Progress bars** during CV processing  

---

## 🧠 How It Works

1. **Upload CV PDFs**  
2. **Paste the Job Description text**  
3. **JD and CVs are chunked** for LLM processing  
4. **LLM scoring** generates:  
   - Sub-bullet requirement evaluation  
   - Must-have vs preferred/optional classification  
   - Detailed project and education analysis  
5. **Streamlit UI** displays:  
   - Candidate name + Score + Rank  
   - Clickable, expandable detailed explanations  
   - Clean hierarchical bullet-point formatting  

---

## 📂 Project Structure

cv-matcher-ai/
│── jd_agent.py # JD chunking & preprocessing
│── cv_agent.py # CV reading & chunking
│── comp_agent.py # LLM comparison & scoring
│── config.py # API keys, model, and system config
│── utils.py # PDF reading, text cleaning, chunking
│── main.py # Backend pipeline
│── requirements.txt # Python dependencies
│── .env # Your API key (ignored by Git)
│── README.md # Project description
│── .gitignore # Ignore sensitive/unnecessary files


---

## ⚙️ Tech Stack

- **Python 3.10+**  
- **Streamlit** for UI  
- **OpenAI GPT models** for CV evaluation  
- **PyPDF2** for PDF parsing  
- **python-dotenv** for environment variables  

---

