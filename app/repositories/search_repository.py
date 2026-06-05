from sqlalchemy import text
from sqlalchemy.orm import Session


def search_chunks(
    db: Session,
    embedding: list[float],
    limit: int = 5,
):
    query = text(
        """
        SELECT
            id,
            journal_id,
            chunk_text,
            embedding <=> CAST(:embedding AS vector)
                AS distance
        FROM chunks
        ORDER BY embedding <=> CAST(:embedding AS vector)
        LIMIT :limit
        """
    )

    result = db.execute(
        query,
        {
            "embedding": str(embedding),
            "limit": limit,
        },
    )

    return result.fetchall()
