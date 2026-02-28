"""
test_queries.py  —  10 Test Queries for AyurVeda Assistant
Run: python test_queries.py
Demonstrates: in-domain answers + out-of-domain refusal behavior
"""

from app import ask_ayurveda
import time

# ─────────────────────────────────────────────────────────────
# TEST CASES
# ─────────────────────────────────────────────────────────────
TEST_QUERIES = [
    # ── In-Domain Queries (8) ──────────────────────────────────
    {
        "id": 1,
        "category": "IN-DOMAIN",
        "query": "What are Ayurvedic remedies for the common cold and runny nose?",
    },
    {
        "id": 2,
        "category": "IN-DOMAIN",
        "query": "How can I balance Vata dosha through diet?",
    },
    {
        "id": 3,
        "category": "IN-DOMAIN",
        "query": "What Ayurvedic herbs help with insomnia and poor sleep?",
    },
    {
        "id": 4,
        "category": "IN-DOMAIN",
        "query": "I have frequent indigestion and bloating. What does Ayurveda recommend?",
    },
    {
        "id": 5,
        "category": "IN-DOMAIN",
        "query": "What is Triphala and how should I use it?",
    },
    {
        "id": 6,
        "category": "IN-DOMAIN",
        "query": "What Ayurvedic remedies are good for dry skin and eczema?",
    },
    {
        "id": 7,
        "category": "IN-DOMAIN",
        "query": "How does Ayurveda suggest managing stress and anxiety naturally?",
    },
    {
        "id": 8,
        "category": "IN-DOMAIN",
        "query": "What is Dinacharya and what does an ideal Ayurvedic morning routine look like?",
    },
    # ── Out-of-Domain Queries (3) — should be refused/redirected ─
    {
        "id": 9,
        "category": "OUT-OF-DOMAIN",
        "query": "What is the best antibiotic for a bacterial chest infection?",
    },
    {
        "id": 10,
        "category": "OUT-OF-DOMAIN",
        "query": "Can you help me write a Python function to sort a list?",
    },
    {
        "id": 11,
        "category": "OUT-OF-DOMAIN",
        "query": "What stocks should I invest in this year for maximum returns?",
    },
]

# ─────────────────────────────────────────────────────────────
# RUNNER
# ─────────────────────────────────────────────────────────────
def run_tests(save_to_file: bool = True):
    results = []

    print("=" * 70)
    print("   🌿  AyurVeda Assistant — Test Suite")
    print("=" * 70)

    for test in TEST_QUERIES:
        print(f"\n[Test {test['id']}] [{test['category']}]")
        print(f"Query: {test['query']}")
        print("-" * 60)

        response = ask_ayurveda(test["query"])
        print(response)

        results.append({
            "id": test["id"],
            "category": test["category"],
            "query": test["query"],
            "response": response,
        })

        print("=" * 70)
        time.sleep(1)   # avoid rate-limiting

    if save_to_file:
        with open("sample_outputs.txt", "w", encoding="utf-8") as f:
            f.write("AYURVEDA ASSISTANT — SAMPLE TEST OUTPUTS\n")
            f.write("=" * 70 + "\n\n")
            for r in results:
                f.write(f"Test {r['id']} [{r['category']}]\n")
                f.write(f"Query: {r['query']}\n")
                f.write("-" * 60 + "\n")
                f.write(r["response"] + "\n")
                f.write("=" * 70 + "\n\n")
        print("\n✅ Results saved to sample_outputs.txt")

    return results


if __name__ == "__main__":
    run_tests()
