SUMMARY_PROMPT = """
Summarize the following content.

Include:
- Main Ideas
- Key Insights
- Important Conclusions

Content:
{text}
"""

QUESTIONS_PROMPT = """
Generate 10 important questions
from the following content.

{text}
"""

NOTES_PROMPT = """
Create detailed study notes.

Include:
- Key Concepts
- Important Facts
- Takeaways

{text}
"""

FLASHCARD_PROMPT = """
Create 15 flashcards.

Format:

Q:
A:

{text}
"""

RAG_PROMPT = """
Answer ONLY from the context.

Context:
{context}

Question:
{question}

If answer is unavailable,
say:
I couldn't find that information.
"""