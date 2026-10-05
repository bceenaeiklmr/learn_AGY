"""
Sample utility module for string manipulation and text processing.
"""

from typing import List


def slugify(text: str) -> str:
    """Converts a string into a URL-friendly slug."""
    import re
    text = text.lower().strip()
    # Replace non-alphanumeric characters with hyphens
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")


def extract_keywords(text: str, min_length: int = 4) -> List[str]:
    """Extracts unique lowercase words greater than or equal to min_length."""
    import re
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    seen = set()
    result = []
    for w in words:
        if len(w) >= min_length and w not in seen:
            seen.add(w)
            result.append(w)
    return result
