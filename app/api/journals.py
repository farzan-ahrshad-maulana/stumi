from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas.journal import (
    JournalCreate,
)
from app.services.journal_service import create_journal
from app.services.metadata_service import (
    extract_metadata,
)
from app.services.pdf_service import (
    download_pdf,
    extract_text,
)

router = APIRouter(prefix="/journals", tags=["journals"])


@router.post("/")
def create_journal_endpoint(
    payload: JournalCreate,
    db: Session = Depends(get_db),
):

    pdf_bytes = download_pdf(payload.pdf_url)

    text = extract_text(pdf_bytes)

    metadata = extract_metadata(text)

    journal = create_journal(
        db=db,
        metadata=metadata,
        pdf_url=payload.pdf_url,
    )

    return {
        "id": journal.id,
        "title": journal.title,
        "status": "saved",
    }
