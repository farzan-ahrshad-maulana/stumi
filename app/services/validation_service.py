from io import BytesIO

from pypdf import PdfReader

from app.core.logger import logger
from app.schemas.metadata import LLMMetadata


def basic_validation(
    text: str,
) -> tuple[bool, str]:

    is_valid, reason = academic_structure_validation(text)

    if not is_valid:
        logger.warning(reason)
        return {
            "status": "rejected",
            "reason": reason,
        }

    if not text.strip():
        return False, "PDF contains no extractable text"

    if len(text) < 5000:
        return False, "Document too short"

    if len(text.split()) < 1000:
        return False, "Not enough words"

    return True, ""


def validate_metadata(
    metadata: LLMMetadata,
) -> tuple[bool, str]:

    if len(metadata.title.strip()) < 10:
        return False, "Invalid title"

    if len(metadata.authors.strip()) < 5:
        return False, "Invalid authors"

    if len(metadata.abstract.strip()) < 300:
        return False, "Abstract too short"

    return True, ""


def academic_structure_validation(
    text: str,
) -> tuple[bool, str]:

    text_lower = text.lower()

    keywords = [
        "abstract",
        "introduction",
        "references",
    ]

    found = sum(1 for keyword in keywords if keyword in text_lower)

    if found < 2:
        return (
            False,
            "Document does not appear to be an academic paper",
        )

    return True, ""


def validate_pdf_url(
    pdf_url: str,
) -> tuple[bool, str]:

    if not pdf_url.startswith("https://"):
        return (
            False,
            "Only HTTPS URLs are allowed",
        )

    if not pdf_url.lower().endswith(".pdf"):
        return (
            False,
            "URL must point to a PDF file",
        )

    return True, ""


def validate_text_pdf(
    pdf_bytes: bytes,
) -> tuple[bool, str]:

    try:
        reader = PdfReader(BytesIO(pdf_bytes))

        pages_to_check = min(
            5,
            len(reader.pages),
        )

        total_chars = 0

        for i in range(pages_to_check):
            text = reader.pages[i].extract_text()

            if text:
                total_chars += len(text.strip())

        if total_chars < 500:
            return (
                False,
                "PDF appears to be image-based or scanned",
            )

        return (
            True,
            "",
        )

    except Exception:
        return (
            False,
            "Invalid PDF file",
        )


def validate_pdf_size(
    pdf_bytes: bytes,
) -> tuple[bool, str]:

    max_size_mb = 25

    file_size_mb = len(pdf_bytes) / (1024 * 1024)

    if file_size_mb > max_size_mb:
        return (
            False,
            f"PDF exceeds maximum size limit ({max_size_mb} MB)",
        )

    return True, ""


def validate_page_count(
    pdf_bytes: bytes,
) -> tuple[bool, str]:

    max_pages = 100

    try:
        reader = PdfReader(BytesIO(pdf_bytes))

        page_count = len(reader.pages)

        if page_count > max_pages:
            return (
                False,
                f"PDF exceeds maximum page limit ({max_pages} pages)",
            )

        return (
            True,
            "",
        )

    except Exception:
        return (
            False,
            "Unable to read PDF",
        )
