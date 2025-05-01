from typing import Any
from typing import Optional
from typing import Union


def get_mask_card_number(number_card: str) -> str:
    """
    Функция get_mask_card_number принимает на вход номер
    карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_card: str) -> str:
    """
    Функция get_mask_account принимает на вход номер
    счета в виде числа и возвращает маску номера по
    правилу **XXXX
    """
    return f"**{number_card[-4:]}"


print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
