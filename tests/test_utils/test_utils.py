import pytest

from src.utils.utils import fetch_text


def test_fetch_text_success():
    url = "https://example.com"
    expected_content = "Example Domain"
    assert expected_content in fetch_text(url)


def test_fetch_text_unreachable_url():
    url = "https://nonexistent.url"
    with pytest.raises(Exception):
        fetch_text(url)


def test_fetch_text_invalid_url():
    with pytest.raises(ValueError):
        fetch_text("not_a_valid_url")
