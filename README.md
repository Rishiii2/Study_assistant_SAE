# AI Study Assistant CLI
### FORGETRACK 2026 — Week 03 — Tech Track

An AI-powered command-line study assistant built with the Gemini API.
Enter any topic to receive a structured study plan, then ask follow-up
questions in a continuing conversation.

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/study-assistant
cd study-assistant
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your Gemini API key from aistudio.google.com
python main.py
```

---

## Prompt Engineering Writeup

### 1. What role did you assign in your system prompt, and why did you choose that framing?

The role assigned is "expert academic tutor and structured learning specialist."
This framing was chosen deliberately over a generic "helpful assistant" because it
anchors the model's behaviour to a specific professional context. A tutor has an
implied obligation to structure information pedagogically — covering prerequisites
before advanced concepts, recommending learning order, and keeping explanations
accessible. The word "specialist" adds a second constraint: the model should not
wander into unrelated topics or produce casual, conversational responses. Together
these two descriptors significantly tighten the output compared to a vague role.

### 2. What format did you specify for the study plan output, and how did you enforce it in the prompt?

The format specified is a numbered list with a fixed header (`STUDY PLAN: [Topic]`),
a divider line of equals signs, one subtopic per line in the format
`N. [Name] — [one sentence description]`, a closing divider, and two footer fields
(recommended order and estimated time). This was enforced by providing the exact
template — including the `=====` lines and the `N. Name — Description` syntax — directly
in the system prompt. The model was additionally told to use "ONLY" this format with
"no deviations," and a hard word limit of 350 words was set to prevent elaboration
beyond the structure. Enforcing format through both an explicit template and a "no
deviations" instruction produces far more consistent output than either approach alone.

### 3. What happens if you remove the system prompt entirely?

Without the system prompt, Gemini responds conversationally with paragraphs of
introductory text before any actual content, adds motivational phrases ("Great choice!",
"Let's get started!"), uses inconsistent formatting across different topics, and
frequently exceeds an appropriate response length. With the engineered system prompt,
every response — regardless of topic — produces the same structured, scannable format
with no filler text. The difference is most visible across topics: with the system
prompt, "Machine Learning" and "Roman History" both produce identically structured
study plans; without it, the format and depth vary wildly between topics.

---

## Features

- Structured study plan generation for any topic
- Continuing chat loop with full session context
- Engineered system prompt with role, format, length, and "do not" constraints
- Session summary on exit (topic studied, questions asked)
- Secure API key handling via `.env` file (never hardcoded)

---

## Files

| File | Purpose |
|------|---------|
| `main.py` | Main CLI application |
| `.env` | API key (not committed to GitHub) |
| `.env.example` | Template showing required environment variables |
| `requirements.txt` | Python dependencies |
| `README.md` | This file — includes prompt engineering writeup |

---

*SAE DTU · FORGETRACK 2026 · Week 03 · Tech Track*
