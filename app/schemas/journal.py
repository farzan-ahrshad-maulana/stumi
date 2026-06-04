from pydantic import BaseModel, ConfigDict


class JournalCreate(BaseModel):
    pdf_url: str


class JournalResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int

    title: str
