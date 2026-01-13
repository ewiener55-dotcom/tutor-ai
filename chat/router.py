from agents import Agent
from .agents import hebrew_tutor, english_tutor

triage = Agent(
    name="Language Router",
    instructions="""
If the user writes Hebrew, handoff to Hebrew Tutor.
If the user writes English, handoff to English Tutor.
Never answer directly.
""",
    handoffs=[hebrew_tutor, english_tutor]
)
