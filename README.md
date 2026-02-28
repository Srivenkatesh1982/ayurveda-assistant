# 🌿 AyurVeda Home Remedies Assistant
### Domain-Specific LLM using OpenRouter + LangChain | Google Colab Ready

> **Reference Book:** *The Complete Book of Ayurvedic Home Remedies* — Vasant Lad  
> **Assignment:** Domain-Specific LLM Assistant using OpenRouter and LangChain

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/ayurveda-assistant/blob/main/AyurVeda_Assistant.ipynb)

---

## 📌 What This Project Does

An AI assistant that answers **only** Ayurvedic home remedy questions. It:
- ✅ Answers dosha, herb, diet, and home remedy questions
- ❌ Refuses all out-of-domain queries (modern medicine, coding, finance)
- 📋 Returns every answer in a consistent 5-section format
- ⚠️ Adds a medical disclaimer to every response
- 💬 Provides an interactive chat widget inside Google Colab

---

## 🗂️ Project Structure

```
ayurveda-assistant/
├── AyurVeda_Assistant.ipynb   ← Main notebook (run this on Colab)
├── app.py                     ← Core logic (LLM + chain + CLI)
├── streamlit_app.py           ← Optional Streamlit UI
├── test_queries.py            ← 11 test cases runner
├── requirements.txt           ← Python dependencies
├── .env.example               ← API key template
└── README.md                  ← This file
```

---

## 🚀 Quick Start — Google Colab (Recommended)

### Option 1: One-Click (after pushing to GitHub)
1. Replace `YOUR_USERNAME` in the badge URL above with your GitHub username
2. Click the **Open in Colab** badge
3. Follow the steps in the notebook

### Option 2: Manual Upload to Colab
1. Go to [colab.research.google.com](https://colab.research.google.com)
2. Click `File` → `Upload notebook`
3. Upload `AyurVeda_Assistant.ipynb`
4. Run cells top to bottom

### Step-by-Step Inside the Notebook
| Step | Cell | What It Does |
|------|------|-------------|
| 1 | Install | `pip install` all packages |
| 2 | API Key | Load from Colab Secrets or getpass |
| 3 | LLM Init | Connect ChatOpenAI → OpenRouter |
| 4 | System Prompt | Define role, domain rules, output format |
| 5 | Chain Build | `prompt | llm | parser` LCEL pipeline |
| 6 | Quick Test | Single query end-to-end test |
| 7 | Test Suite | All 11 queries, saves sample_outputs.txt |
| 8 | Download | Download results for submission |
| 9 | Chat Widget | Live interactive ipywidgets chat UI |
| 10 | Summary | Project architecture overview |

---

## 🔑 API Key Setup

### Get a Free Key
1. Go to [openrouter.ai/keys](https://openrouter.ai/keys)
2. Sign up (free) → Create API Key
3. Copy the key (starts with `sk-or-...`)

### Add to Colab Secrets (Recommended — Key Never Visible)
1. In Colab, click the 🔑 **key icon** in the left sidebar
2. Click `+ Add new secret`
3. **Name:** `OPENROUTER_API_KEY`
4. **Value:** your key
5. Toggle the switch **ON**

### Alternative: getpass (Quick — Not Saved)
The notebook automatically falls back to a hidden password prompt if Secrets are not configured.

---

## 🧪 Test Cases

| # | Category | Query |
|---|----------|-------|
| 1 | ✅ In-Domain | Ayurvedic remedies for common cold |
| 2 | ✅ In-Domain | How to balance Vata dosha |
| 3 | ✅ In-Domain | Herbs for insomnia |
| 4 | ✅ In-Domain | Indigestion and bloating remedies |
| 5 | ✅ In-Domain | What is Triphala? |
| 6 | ✅ In-Domain | Dry skin and eczema remedies |
| 7 | ✅ In-Domain | Managing stress with Ayurveda |
| 8 | ✅ In-Domain | What is Dinacharya? |
| 9 | ❌ Out-of-Domain | Best antibiotic for chest infection |
| 10 | ❌ Out-of-Domain | Write a Python sorting function |
| 11 | ❌ Out-of-Domain | Stock investment advice |

---

## 📋 Output Format (Every In-Domain Response)

```
🌿 Ayurvedic Perspective:
[Explains the Ayurvedic view of the condition]

🔥 Dosha Involvement:
[Identifies Vata / Pitta / Kapha and explains why]

🌱 Recommended Home Remedies:
[2–4 actionable remedies with instructions]

🍽️ Dietary Suggestions:
[Foods to favour and foods to avoid]

⚠️ Disclaimer:
These are traditional Ayurvedic home remedies for general wellness only...
```

---

## 🛠️ Tech Stack

| Component | Tool |
|-----------|------|
| LLM Gateway | OpenRouter API |
| LLM Model | `mistralai/mistral-7b-instruct` (free) |
| Framework | LangChain (ChatPromptTemplate + LCEL) |
| Language | Python 3.10+ |
| Notebook | Google Colab |
| Optional UI | Streamlit |

---

## ⚙️ Prompt Engineering Elements

1. **Role Definition** — Named assistant + knowledge source (Vasant Lad's book)
2. **Domain Boundaries** — Explicit ✔ allowed topics list
3. **Refusal Rules** — Explicit ✘ forbidden topics with redirect instructions
4. **Structured Output** — 5 mandatory sections enforced in every response
5. **Tone Control** — Warm, educational, non-diagnostic
6. **Mandatory Disclaimer** — Medical safety notice in every response

---

## ⚠️ Medical Disclaimer

This assistant provides **traditional Ayurvedic information for educational purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical concerns.

---

## 🙏 Acknowledgements

- *The Complete Book of Ayurvedic Home Remedies* by Vasant Lad
- [OpenRouter](https://openrouter.ai) for LLM API access
- [LangChain](https://python.langchain.com) for the chain framework
