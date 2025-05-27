from datetime import datetime

from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(account_part: str) -> str:
    """
    Функция, которая умеет обрабатывать информацию о картах и счетах
    """
    account_str = account_part.split()
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
    try:
        # Пробуем проанализировать дату
        parsed_date = datetime.strptime(date[:10], "%Y-%m-%d")
        # Получаем дату в нужном формате
        return parsed_date.strftime("%d.%m.%Y")
    except ValueError:
        # Если формат даты некорректен, выбрасываем наше исключение
        raise ValueError("Некорректный формат даты!")
