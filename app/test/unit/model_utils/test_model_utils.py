import pytest
from unittest.mock import Mock, patch
from app.model_utils.model_utils import encode_text
from app.model_utils import model_utils


# Mocking the Tokenizer class
tokenizer_mock = Mock()


@patch("app.model_utils.model_utils.tokenizer", tokenizer_mock)
def test_encode_text_success():
    # Mocking the encode method to return expected result
    tokenizer_mock.encode.return_value.ids = [1, 2, 3]  # Mocking encoded text ids
    result = encode_text("sample text", num_tokens=10)
    assert result is None  # Since the function returns nothing


@patch("app.model_utils.model_utils.tokenizer", tokenizer_mock)
def test_encode_text_exception():
    # Mocking the encode method to raise an exception
    tokenizer_mock.encode.side_effect = Exception("Tokenization failed")
    with pytest.raises(ValueError):
        encode_text("sample text", num_tokens=10)
    # reset the state
    tokenizer_mock.encode.side_effect = None


@patch("app.model_utils.model_utils.tokenizer", tokenizer_mock)
def test_encode_text_updated_tokens():
    # Mocking the encode method to return expected result
    tokenizer_mock.encode.return_value.ids = [1, 2, 3]  # Mocking encoded text ids
    encode_text("sample text", num_tokens=10)
    assert model_utils.DummyModel.tokens == [2, 3]  # Check if tokens were updated


@patch("app.model_utils.model_utils.tokenizer", tokenizer_mock)
def test_encode_text_updated_num_tokens():
    # Mocking the encode method to return expected result
    tokenizer_mock.encode.return_value.ids = [1, 2, 3]  # Mocking encoded text ids
    encode_text("sample text", num_tokens=42)
    assert model_utils.DummyModel.num_tokens == 42  # Check if num_tokens was updated
