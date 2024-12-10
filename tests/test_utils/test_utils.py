import pytest

from src.utils.utils import fetch_text


@pytest.mark.parametrize(
    "url,expected_content",
    [("https://example.com", "Example Domain"), ("https://google.com", "Google")],
)
def test_fetch_text_success(url, expected_content):
    assert expected_content in fetch_text(url)


def test_fetch_text_unreachable_url():
    url = "https://nonexistent.url"
    with pytest.raises(Exception):
        fetch_text(url)


def test_fetch_text_invalid_url():
    with pytest.raises(ValueError):
        fetch_text("not_a_valid_url")
