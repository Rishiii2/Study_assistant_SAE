import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

# ============================================================
#  SYSTEM PROMPT — The most important part of this project
#  This is what's actually being graded (35/100 points)
# ============================================================

SYSTEM_PROMPT = """
You are an expert academic tutor and structured learning specialist.
Your sole purpose is to help students master any topic through clear,
organized study plans and concise, precise explanations.

When a student gives you a topic for the first time, respond ONLY with
a structured study plan using this EXACT format — no deviations:

STUDY PLAN: [Topic Name]
=====================================
1. [Subtopic Name] — [One sentence: what this covers and why it matters]
2. [Subtopic Name] — [One sentence: what this covers and why it matters]
3. [Subtopic Name] — [One sentence: what this covers and why it matters]
4. [Subtopic Name] — [One sentence: what this covers and why it matters]
5. [Subtopic Name] — [One sentence: what this covers and why it matters]
(add up to 8 subtopics maximum)
=====================================
RECOMMENDED ORDER: Study these in the numbered sequence above.
ESTIMATED TIME: [Realistic time estimate for a student]

Rules you must ALWAYS follow:
- Do NOT include greetings, motivational phrases, or filler text
- Do NOT exceed 350 words in the study plan response
- Do NOT assume the student's level — keep explanations accessible
- Do NOT start sentences with "I" or refer to yourself
- When answering follow-up questions, be concise — maximum 150 words
  unless a code example or step-by-step process genuinely requires more
- Always be factual, specific, and actionable
"""

# ============================================================
#  MODEL SETUP
# ============================================================

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT
)

chat = model.start_chat(history=[])

# ============================================================
#  MAIN FUNCTION
# ============================================================

def main():
    print("=" * 52)
    print("    AI STUDY ASSISTANT  —  Powered by Gemini")
    print("=" * 52)
    print("  Enter any subject or topic to get a study plan.")
    print("  Then ask follow-up questions about any subtopic.")
    print("  Type 'quit' or 'exit' to end and see your summary.")
    print("=" * 52 + "\n")

    topic_studied = None
    questions_asked = 0
    first_message = True

    while True:
        # Prompt label changes after first message
        if first_message:
            user_input = input("Topic  ▶  ").strip()
        else:
            user_input = input("\nYou    ▶  ").strip()

        # Skip empty inputs
        if not user_input:
            print("         Please type something!\n")
            continue

        # Exit command check
        if user_input.lower() in ["quit", "exit", "q"]:
            print("\n" + "=" * 52)
            print("              SESSION SUMMARY")
            print("=" * 52)
            print(f"  Topic studied   :  {topic_studied if topic_studied else 'None entered'}")
            print(f"  Questions asked :  {questions_asked}")
            print("=" * 52)
            print("  Great study session! Keep learning. 🚀")
            print("=" * 52 + "\n")
            break

        # Track first topic
        if first_message:
            topic_studied = user_input
            first_message = False
        else:
            questions_asked += 1

        # Send to Gemini and display response
        try:
            print("\n  Thinking...\n")
            response = chat.send_message(user_input)
            print("─" * 52)
            print(response.text)
            print("─" * 52)

        except Exception as e:
            print(f"\n  [API Error: {e}]")
            print("  Check your internet connection or API key.\n")


if __name__ == "__main__":
    main()
