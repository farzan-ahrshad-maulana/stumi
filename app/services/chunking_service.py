from dataclasses import dataclass

CHUNK_SIZE = 200
CHUNK_OVERLAP = 40


@dataclass
class TextChunk:
    text: str
    index: int


def chunk_text(text: str) -> list[TextChunk]:

    words = text.split()

    chunks = []

    start = 0
    index = 0

    while start < len(words):


        chunk_words = words[start:end]

        chunks.append(
            TextChunk(
                text=" ".join(chunk_words),
                index=index,
            )
        )

        start += CHUNK_SIZE - CHUNK_OVERLAP

        index += 1

    return chunks
