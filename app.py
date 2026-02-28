"""
Ayurvedic Home Remedies LLM Assistant
Domain-Specific AI using OpenRouter API + LangChain
Reference: The Complete Book of Ayurvedic Home Remedies by Vasant Lad
"""

import os
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv

# ─────────────────────────────────────────────
# 1. Load environment variables
# ─────────────────────────────────────────────
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
MODEL_NAME = "mistralai/mistral-7b-instruct"   # free-tier friendly on OpenRouter


# ─────────────────────────────────────────────
# 2. Initialise the LLM via OpenRouter
# ─────────────────────────────────────────────
def get_llm(temperature: float = 0.4) -> ChatOpenAI:
    """
    Returns a LangChain ChatOpenAI instance pointed at OpenRouter.

    Why ChatOpenAI?
    ---------------
    OpenRouter exposes an OpenAI-compatible REST API, so LangChain's
    ChatOpenAI class works perfectly by simply changing the base_url
    and injecting the OpenRouter key.
    """
    return ChatOpenAI(
        model=MODEL_NAME,
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base=OPENROUTER_BASE_URL,
        temperature=temperature,
    )


# ─────────────────────────────────────────────
# 3. System Prompt  ← Core Prompt Engineering
# ─────────────────────────────────────────────
SYSTEM_PROMPT = """
You are AyurVeda Assistant — a friendly, knowledgeable Ayurvedic Home Remedy advisor.
Your knowledge is strictly based on classical Ayurvedic principles as described in
"The Complete Book of Ayurvedic Home Remedies" by Vasant Lad.

════════════════════════════════════════════════
ROLE & EXPERTISE
════════════════════════════════════════════════
• Expert in Ayurvedic concepts: Vata, Pitta, Kapha doshas, Prakriti, Agni, Ama.
• Knowledgeable about herbs (e.g., ashwagandha, triphala, tulsi, neem, ginger),
  dietary guidelines, lifestyle routines (Dinacharya), and home remedies.
• Guides users to balance their doshas through food, herbs, and daily habits.

════════════════════════════════════════════════
DOMAIN BOUNDARIES  (what you WILL answer)
════════════════════════════════════════════════
✔ Common ailments addressed by Ayurvedic home remedies
  (cold, indigestion, insomnia, stress, skin issues, joint pain, etc.)
✔ Dosha identification and balancing tips
✔ Ayurvedic diet and food recommendations
✔ Herbal preparations and their uses
✔ Ayurvedic daily & seasonal routines
✔ General Ayurvedic concepts and philosophy

════════════════════════════════════════════════
OUT-OF-DOMAIN TOPICS  (what you will NOT answer)
════════════════════════════════════════════════
✘ Allopathic / modern medicine diagnoses or prescriptions
✘ Surgical procedures or emergency medical advice
✘ Mental health clinical therapy (depression, schizophrenia treatment)
✘ Financial, legal, or technical (coding) queries
✘ Any topic unrelated to Ayurvedic home remedies

If a query falls outside the domain, politely refuse and redirect.

════════════════════════════════════════════════
OUTPUT FORMAT  (always follow this structure)
════════════════════════════════════════════════
**🌿 Ayurvedic Perspective:**
[Briefly explain the Ayurvedic view of the condition/question]

**🔥 Dosha Involvement:**
[Identify which dosha(s) are affected — Vata / Pitta / Kapha]

**🌱 Recommended Home Remedies:**
[List 2–4 specific, actionable Ayurvedic remedies]

**🍽️ Dietary Suggestions:**
[Foods to favour and foods to avoid]

**⚠️ Disclaimer:**
These are traditional Ayurvedic home remedies for general wellness only.
They are NOT a substitute for professional medical advice.
Please consult a qualified healthcare provider for serious conditions.

════════════════════════════════════════════════
TONE
════════════════════════════════════════════════
• Warm, supportive, and educational.
• Use simple language; explain Sanskrit terms briefly when used.
• Never diagnose; always frame as "Ayurveda suggests…" or "traditionally used for…".
"""


# ─────────────────────────────────────────────
# 4. Prompt Template (LangChain)
# ─────────────────────────────────────────────
def get_prompt_template() -> ChatPromptTemplate:
    """
    Constructs a ChatPromptTemplate with:
      - SystemMessage : role definition, domain rules, output format
      - HumanMessage  : the user's actual query
    """
    return ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{user_query}"),
    ])


# ─────────────────────────────────────────────
# 5. LLM Chain
# ─────────────────────────────────────────────
def build_chain(temperature: float = 0.4):
    """
    Builds the LangChain LCEL chain:
      prompt_template | llm | output_parser
    """
    llm = get_llm(temperature)
    prompt = get_prompt_template()
    parser = StrOutputParser()
    return prompt | llm | parser


# ─────────────────────────────────────────────
# 6. Query Function
# ─────────────────────────────────────────────
def ask_ayurveda(query: str, temperature: float = 0.4) -> str:
    """
    Main entry point.  Pass any query; the chain handles domain control.

    Args:
        query       : User's question (string)
        temperature : LLM creativity level (0.0 – 1.0; default 0.4)

    Returns:
        str : Formatted Ayurvedic response
    """
    chain = build_chain(temperature)
    return chain.invoke({"user_query": query})


# ─────────────────────────────────────────────
# 7. CLI Interface
# ─────────────────────────────────────────────
def main():
    print("=" * 60)
    print("   🌿  AyurVeda Home Remedies Assistant  🌿")
    print("   Powered by OpenRouter + LangChain")
    print("   Reference: The Complete Book of Ayurvedic Home Remedies")
    print("=" * 60)
    print("Type your question (or 'quit' to exit)\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("quit", "exit", "q"):
            print("Namaste! 🙏 Stay healthy!")
            break
        if not user_input:
            continue
        print("\nAssistant:\n")
        response = ask_ayurveda(user_input)
        print(response)
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()
