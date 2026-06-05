from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str


class ChatRequest(BaseModel):
    journal_id: int
    question: str
