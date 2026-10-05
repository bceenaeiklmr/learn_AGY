"""
Pytest unit tests for app.py.
"""

from app import slugify, extract_keywords


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_special_characters():
    assert slugify("Learn Antigravity (Agy) 2026!") == "learn-antigravity-agy-2026"


def test_slugify_spaces_and_hyphens():
    assert slugify("   Multiple   Spaces   ") == "multiple-spaces"


def test_extract_keywords():
    text = "Antigravity empowers agents to write Python and AutoHotkey code efficiently"
    keywords = extract_keywords(text, min_length=6)
    assert "antigravity" in keywords
    assert "empowers" in keywords
    assert "agents" in keywords
    assert "autohotkey" in keywords
    assert "efficiently" in keywords
    assert "code" not in keywords  # length 4 < 6
