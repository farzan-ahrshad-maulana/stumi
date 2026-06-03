from io import BytesIO

import requests
from pypdf import PdfReader


def download_pdf(url: str) -> bytes:
    response = requests.get(
        url,
        timeout=30,
    )

    response.raise_for_status()

    return response.content


def extract_text(pdf_bytes: bytes) -> str:

    pdf_stream = BytesIO(pdf_bytes)

    reader = PdfReader(pdf_stream)

    pages = []

    for page in reader.pages:
        text = page.extract_text()

        if text:
            pages.append(text)

    return "\n".join(pages)
