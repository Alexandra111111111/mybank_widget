from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_str: str) -> str:
    """
    Функция, которая умеет обрабатывать информацию о картах и счетах
    """
    account_str = account_str.split(maxsplit=-1)
    # print(account_str)
    if len(account_str[-1]) == 20:
        return f"{account_str[0]} {get_mask_account(account_str[-1])}"
    elif len(account_str[-1]) < 20 and len(account_str) > 2:
        return f"{' '.join(account_str[:2])} {get_mask_card_number(account_str[-1])}"
    else:
        return f"{account_str[0]} {get_mask_card_number(account_str[-1])}"


def get_date(date: str) -> str:
    """
    Функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date = date[:10].split("-")[::-1]
    return ".".join(date)

a = "Visa Platinum 7000792289606361"
b = "Maestro 7000792289606361"
c = "Счет 73654108430135874305"

vh_1 = "Maestro 1596837868705199"
vh_2 = "Счет 64686473678894779589"
vh_3 = "MasterCard 7158300734726758"
vh_4 = "Счет 35383033474447895560"
vh_5 = "Visa Classic 6831982476737658"
vh_6 = "Visa Platinum 8990922113665229"
vh_7 = "Visa Gold 5999414228426353"
vh_8 = "Счет 73654108430135874305"

my_date = "2024-03-11T02:26:18.671407"

print(mask_account_card(a))
print(mask_account_card(b))
print(mask_account_card(c))
print(mask_account_card(vh_1))
print(mask_account_card(vh_2))
print(mask_account_card(vh_3))
print(mask_account_card(vh_4))
print(mask_account_card(vh_5))
print(mask_account_card(vh_6))
print(mask_account_card(vh_7))
print(mask_account_card(vh_8))

print(get_date(my_date))