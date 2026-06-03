from app.services.pdf_service import (
    download_pdf,
    extract_text,
)

pdf = download_pdf("https://arxiv.org/pdf/1706.03762.pdf")

text = extract_text(pdf)

print(text[:2000])
