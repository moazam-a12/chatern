# Chatern: Internship Support Chatbot

Chatern is an AI-powered chatbot designed to support interns by answering their FAQs related to HR, IT, onboarding, and project reporting.  
It leverages **Google Gemini API** and a custom dataset of **6,000 synthetic Q&A pairs** to simulate fine-tuning and provide context-aware responses.  
This project demonstrates professional project structuring, data preprocessing, and integration with a modern LLM.

---

## Project Structure

```
Chatbot for Internship Support/
│
├── data/
│   └── intern_support_finetune_gemini.jsonl   # 6k Q&A dataset
│
├── model/
│   └── gemini_service.py                     # Gemini service (API + chatbot logic)
│
└── chatern.ipynb                             # Main notebook (UI + workflow)
```

---

## Features

- **Dataset:** 6,000 synthetic intern support questions & answers  
- **Gemini API Integration:** Uses free-tier `gemini-1.5-flash`  
- **Context Injection:** Simulates fine-tuning by feeding dataset examples  
- **Notebook UI:** Chatbox with bubbles (via `ipywidgets`)  
- **Modular Codebase:** `gemini_service.py` handles logic, notebook is clean driver  
- **Interactive Chat:** Ask Chatern anything related to internship support  

---

## Setup & Installation

1. Clone or download this repository.  
2. Open `chatern.ipynb` in Jupyter Notebook / JupyterLab.  
3. Install required dependencies in the **first cell**:

```bash
!pip install google-genai pandas ipywidgets matplotlib
```

4. (One-time setup for widgets)
```bash
jupyter nbextension enable --py widgetsnbextension
```

5. Insert your **Gemini API key** into the notebook:
```python
API_KEY = "YOUR_API_KEY"
```

---

## Usage

- Run `chatern.ipynb` step by step.  
- Preview dataset with:
```python
chatern.preview_dataset(3)
```
- Ask a single question:
```python
chatern.ask("When is the weekly report due?")
```
- Use the interactive **chatbox UI** (with bubbles!) to chat with Chatern in real-time.  

---

## Limitations

- **Requires Internet:** Gemini API calls need an active internet connection.  
- **API Key:** A valid Gemini API key is required.  
- **Fine-tuning:** Real Gemini fine-tuning is only available on paid tiers. In this project, we **simulate fine-tuning** using context injection.  
- **Not Perfect:** Since it's simulated, responses may occasionally be generic.  
- **Demo Dataset:** The 6k Q&A dataset is synthetic and meant for demonstration purposes only.  

---

## Future Improvements

- Implement **real fine-tuning** with Google Vertex AI.  
- Add **retrieval-augmented generation (RAG)** for smarter, scalable FAQ search.  
- Deploy Chatern to **Slack/Teams/Discord** for real intern usage.  
- Build a **web UI** using Streamlit or Flask for a professional chatbot experience.  

---

## Disclaimer  

Chatern is not responsible for:  
- Late reports 🕒  
- Cold coffee ☕  
- HR ignoring your emails 📧  

But it *is* responsible for making your internship journey 10x cooler 😉
