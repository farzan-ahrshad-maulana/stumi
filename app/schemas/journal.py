from pydantic import BaseModel


class JournalCreate(BaseModel):
    pdf_url: str
