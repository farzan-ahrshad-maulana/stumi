from sqlalchemy.orm import Session

from app.services.llm_service import (
    generate_answer,
)
from app.services.retrieval_service import (
    retrieve_chunks,
)


def ask_question(
    db: Session,
    question: str,
):

    results = retrieve_chunks(
        db=db,
        question=question,
        limit=5,
    )

    context = "\n\n".join(row.chunk_text for row in results)

    answer = generate_answer(
        question=question,
        context=context,
    )

    return answer
