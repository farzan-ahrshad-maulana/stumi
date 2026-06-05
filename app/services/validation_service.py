def basic_validation(
    text: str,
):

    if not text.strip():
        return False, "PDF contains no extractable text"

    if len(text) < 5000:
        return False, "Document too short"

    if len(text.split()) < 1000:
        return False, "Not enough words"

    return True, None
