from sqlalchemy.orm import Session

from app.db.models import Chunk


def create_chunk(
    db: Session,
    journal_id: int,
    chunk_text: str,
    embedding: list[float],
    chunk_index: int,
) -> Chunk:

    chunk = Chunk(
        journal_id=journal_id,
        chunk_text=chunk_text,
        embedding=embedding,
        chunk_index=chunk_index,
    )

    db.add(chunk)

    return chunk
