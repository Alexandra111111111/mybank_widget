from typing import List, Dict, Iterator

def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Возвращает итератор, генерирующий транзакции, выполненные в заданной валюте.

    :param transactions: Список словарей с данными транзакций.
    :param currency_code: Валюта, по которой производится выборка.
    :return: Итератор, содержащий подходящие транзакции.
    """
    return (tx for tx transactions if tx["operationAmount"]["currency"]["code"] == currency_code)

