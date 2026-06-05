from sqlalchemy.orm import Session

from app.repositories.chunk_repository import (
    create_chunk,
)
from app.services.chunking_service import (
    chunk_text,
)
from app.services.embedding_service import (
    create_embedding,
)


def store_chunks(
    db: Session,
    journal_id: int,
    text: str,
) -> int:

    chunks = chunk_text(text)

    for chunk in chunks:
        embedding = create_embedding(chunk.text)

        create_chunk(
            db=db,
            journal_id=journal_id,
            chunk_text=chunk.text,
            embedding=embedding,
            chunk_index=chunk.index,
        )

    db.commit()

    return len(chunks)
