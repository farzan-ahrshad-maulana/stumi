from app.db.database import SessionLocal
from app.services.rag_service import (
    ask_question,
)

db = SessionLocal()

answer = ask_question(
    db=db,
    question="What is the Transformer architecture?",
)

print(answer)
