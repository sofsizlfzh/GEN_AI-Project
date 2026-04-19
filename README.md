# ✉️ Smart Email & Letter Generator — Generative AI-2 Project

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Google_Gemini-1.5_Flash-4285F4?style=for-the-badge&logo=google&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

*Instantly craft professional emails, cover letters, and formal applications using the power of Generative AI.*

</div>

---

## 📌 Project Overview

**Smart Email & Letter Generator** is a full-stack Generative AI application built for the **Generative AI-2** university course. It solves a real-world productivity problem: the time, effort, and skill required to write polished professional communication.

Using **Google Gemini 1.5 Flash** as the backbone LLM, advanced **prompt engineering** techniques, and a clean **Streamlit** GUI, the app allows any user — regardless of writing skill — to produce high-quality, context-aware documents in seconds.

---

## 🧠 Problem Definition

### Why Smart Email Generation Matters

Every day, millions of professionals, students, and job seekers face the same challenge:

| Pain Point | Impact |
|---|---|
| ⏱ Writing a single professional email takes 15–45 minutes | Lost productivity; missed opportunities |
| 😓 Wrong tone or phrasing damages professional relationships | Career setbacks; lost clients |
| 🌐 Non-native English speakers struggle with formal language | Systematic disadvantage |
| 📄 Cover letters require specific structural knowledge | Good candidates get rejected on form |
| 🔁 Repetitive communication tasks drain cognitive energy | Burnout; lower quality over time |

**Our Solution:** A prompt-engineered AI assistant that takes structured user input and instantly produces publication-ready professional documents — with full control over tone, length, language, and content focus.

---

## ✨ Features

- **8 Document Types** — Professional Email, Cover Letter, Formal Application, Apology Letter, Networking Email, Complaint Letter, Business Proposal, Thank-You Letter
- **6 Tone Modes** — Professional, Friendly, Urgent, Persuasive, Formal, Empathetic
- **4 Length Settings** — Short (~100w) to Long (~500w)
- **7 Languages** — English, Hindi, Spanish, French, German, Arabic, Japanese
- **Creativity Slider** — Maps to LLM temperature for output control
- **Session History** — Revisit up to 5 previously generated documents
- **One-Click Download** — Export as `.txt` or `.md`
- **Copy-Ready Output Area** — Pre-filled text area for instant clipboard copy
- **Robust Error Handling** — Clear messages for invalid keys, quota errors, safety blocks

---

## 🏛️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        STREAMLIT FRONTEND                        │
│                                                                   │
│  ┌──────────────┐          ┌──────────────────────────────────┐  │
│  │   SIDEBAR    │          │          MAIN PANEL              │  │
│  │              │          │                                  │  │
│  │ • API Key    │          │  LEFT COL       RIGHT COL        │  │
│  │ • Creativity │          │  ─────────      ──────────       │  │
│  │ • Language   │          │  Doc Type       Output Area      │  │
│  │ • Tips       │          │  Sender Name    Word Count       │  │
│  └──────────────┘          │  Recipient      Download Btns    │  │
│                            │  Subject        Copy Area        │  │
│                            │  Key Points     History          │  │
│                            │  Tone           ────────         │  │
│                            │  Length                          │  │
│                            └──────────────────────────────────┘  │
└───────────────────────────────────┬─────────────────────────────┘
                                    │  User Inputs
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                   PROMPT ENGINEERING LAYER                       │
│                                                                   │
│  build_prompt()                                                   │
│  ├─ System Role:    "You are an expert professional writer…"     │
│  ├─ Task:           Doc type + all parameters                    │
│  ├─ Tone Directive: Injected from TONE_MAP dictionary            │
│  ├─ Content Hints:  Key points + extra context                   │
│  └─ Constraints:    Word count, language, format rules           │
└───────────────────────────────────┬─────────────────────────────┘
                                    │  Structured prompt string
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                   GOOGLE GEMINI 1.5 FLASH API                    │
│                                                                   │
│  GenerativeModel.generate_content()                              │
│  ├─ Temperature:     User-controlled (0.0 – 1.0)                 │
│  ├─ Max Tokens:      1024 (cost-safe ceiling)                    │
│  ├─ Top-P:           0.9 (nucleus sampling)                      │
│  └─ Top-K:           40                                          │
└───────────────────────────────────┬─────────────────────────────┘
                                    │  Generated text
                                    ▼
┌─────────────────────────────────────────────────────────────────┐
│                   OUTPUT & PERSISTENCE LAYER                     │
│                                                                   │
│  • Styled HTML output area (pre-wrap, scrollable)                │
│  • Word / character count + read-time metrics                    │
│  • st.session_state history (5-item circular buffer)             │
│  • Download as .txt / .md                                        │
└─────────────────────────────────────────────────────────────────┘
```

### Generative AI Concepts Applied

| Concept | Implementation |
|---|---|
| **Prompt Engineering** | Structured system + task + constraint prompts in `build_prompt()` |
| **Zero-shot Inference** | Model generates documents with no examples — only instructions |
| **Temperature Control** | Sidebar slider maps directly to `generation_config.temperature` |
| **Token Budgeting** | `max_output_tokens=1024` balances quality vs. cost |
| **Nucleus Sampling** | `top_p=0.9` used alongside temperature for quality output |
| **Role Prompting** | Model instructed to BE an expert writer, not just act like one |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **GUI Framework** | Streamlit 1.35+ |
| **AI Model** | Google Gemini 1.5 Flash |
| **AI SDK** | `google-generativeai` |
| **Notebook Env** | Google Colab / Jupyter |
| **Tunneling** | localtunnel / ngrok (Colab) |

---

## 🚀 Installation & Usage

### Option A: Run Locally (Recommended for Development)

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/smart-email-generator.git
cd smart-email-generator

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

### Option B: Run in Google Colab (Zero Local Setup)

This is the primary deployment method for the university submission.

**Step 1:** Open the notebook in Colab  
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/smart-email-generator/blob/main/Smart_Email_Generator_GenAI2.ipynb)

**Step 2:** Run **Cell 1** — installs `streamlit`, `google-generativeai`, `localtunnel`

**Step 3:** Run **Cell 2** — uses `%%writefile app.py` magic command to save the app

**Step 4:** Run **Cell 3** — starts Streamlit + localtunnel, prints a public URL

```
✅ App is LIVE at: https://xxxxx.loca.lt
🔑 Tunnel password (if prompted): 34.87.XXX.XXX
```

**Step 5:** Click the URL → enter the IP as password → use the app!

> 💡 **ngrok alternative:** If localtunnel is slow, run **Cell 4** with your free ngrok token from [ngrok.com](https://ngrok.com)

---

### Getting Your Gemini API Key (Free)

1. Visit [aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy the key (starts with `AIza…`)
5. Paste it in the app's sidebar — **it is never stored or logged**

---

## 📁 Repository Structure

```
smart-email-generator/
│
├── app.py                              # Main Streamlit application
├── Smart_Email_Generator_GenAI2.ipynb  # Google Colab notebook
├── requirements.txt                    # Python dependencies
├── README.md                           # This file
├── presentation/
│   └── outline.md                      # Presentation slide outline
└── assets/
    └── screenshot.png                  # App screenshot (optional)
```

---

## 📦 Requirements

```txt
streamlit>=1.35.0
google-generativeai>=0.7.0
```

Save as `requirements.txt` in the project root.

---

## 🔍 Key Code Modules

### `build_prompt()` — The Heart of the App
Assembles a structured prompt from 10 input parameters. Uses role assignment, tone injection from `TONE_MAP`, and explicit format constraints to guarantee high-quality, consistent output.

### `generate_email()` — Gemini API Interface  
Wraps the SDK call with robust error handling for 5 failure modes (invalid key, quota exceeded, safety block, network error, generic exception). Returns clean error strings to the UI.

### `render_sidebar()` — Configuration Panel  
Returns a config dict: API key, temperature, language. Keeps all configuration concerns separate from the main layout.

### `init_session_state()` — State Management  
Initialises all `st.session_state` keys on first run, preventing `KeyError` on Streamlit's multi-rerun execution model.

---

## 🔮 Future Enhancements

- [ ] **RAG Integration** — Upload a CV/resume to auto-populate key points for cover letters
- [ ] **Email Thread Awareness** — Paste a received email and generate a contextual reply
- [ ] **LangChain Memory** — Multi-turn conversation for iterative refinement
- [ ] **Template Library** — Save and reuse custom tone/format templates
- [ ] **Direct Gmail/Outlook Integration** — One-click "Send" via OAuth
- [ ] **A/B Testing Mode** — Generate 2 variants for the same parameters side-by-side
- [ ] **Readability Score** — Flesch-Kincaid grade level displayed alongside metrics
- [ ] **Voice Input** — Whisper API integration for hands-free key-point dictation

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgements

- [Google Gemini](https://ai.google.dev/) for the powerful, accessible LLM API
- [Streamlit](https://streamlit.io/) for the rapid, Python-native GUI framework
- Gen AI-2 course instructors for the project framework and guidance

---

<div align="center">
Built with ❤️ by <strong>Aditya</strong> | Generative AI-2 University Project
</div>
