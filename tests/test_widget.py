from typing import Type

import pytest

from src.widget import get_date
from src.widget import mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-12-31T23:59:59.999999", "31.12.2025"),
        ("2020-01-01T00:00:00.000000", "01.01.2020"),
        ("2023-04-15T12:34:56.789012", "15.04.2023"),
        ("2021-06-22T18:45:30.123456", "22.06.2021"),
        ("2022-09-09T09:09:09.090909", "09.09.2022"),
        ("2023-11-30T23:59:59.999999", "30.11.2023"),
        ("2024-02-29T00:00:00.000000", "29.02.2024"),
        ("2025-07-04T12:00:00.000000", "04.07.2025"),
        ("2026-08-15T15:30:45.678901", "15.08.2026"),
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected


@pytest.mark.parametrize(
    "value, expected_exception",
    [
        ("InvalidDateString", ValueError),  # Некорректная строка
        ("2023-13-32T00:00:00.000000", ValueError),  # Неверный месяц и день
        ("2023-02-30T00:00:00.000000", ValueError),  # Невозможная дата
        ("", ValueError),  # Пустая строка
    ],
)
def test_get_date_error_handling(value: str, expected_exception: Type[ValueError]) -> None:
    with pytest.raises(expected_exception):
        get_date(value)
