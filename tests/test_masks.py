from src.masks import get_mask_card_number
from src.masks import get_mask_account
import pytest


@pytest.mark.parametrize(
    "value, expected",
    [
        ("7000792289606361", 19),
        ("1596837868705199", 19),
        ("7158300734726758", 19),
        ("6831982476737658", 19),
        ("8990922113665229", 19),
        ("5999414228426353", 19),
    ],
)
def test_len_mask_card_number(value, expected):
    assert len(get_mask_card_number(value)) == expected


def test_get_mask_card_number(mask_card_number):
    assert get_mask_card_number("7000792289606361") == mask_card_number
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("700079228960 qqq")
    assert str(exc_info.value) == "Номер карты должен состоять из цифр"
    with pytest.raises(ValueError) as exc_info:
        get_mask_card_number("")
    assert str(exc_info.value) == "Номер карты должен состоять из 16 символов"


@pytest.mark.parametrize(
    "value, expected", [("73654108430135874305", 6), ("64686473678894779589", 6), ("35383033474447895560", 6)]
)
def test_len_get_mask_account(value, expected):
    assert len(get_mask_account(value)) == expected


def test_get_mask_account(mask_account):
    assert get_mask_account("73654108430135874305") == mask_account
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("7365410843013587 qqq")
    assert str(exc_info.value) == "Номер карты должен состоять из цифр"
    with pytest.raises(ValueError) as exc_info:
        get_mask_account("")
    assert str(exc_info.value) == "Номер карты должен состоять из 20 символов"
