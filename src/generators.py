from typing import List, Dict, Iterator

def filter_by_currency(transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """
    Возвращает итератор, генерирующий транзакции, выполненные в заданной валюте.

    :param transactions: Список словарей с данными транзакций.
    :param currency_code: Валюта, по которой производится выборка.
    :return: Итератор, содержащий подходящие транзакции.
    """
    return (tx for tx in transactions if tx["operationAmount"]["currency"]["code"] == currency_code)


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """
    Генерирует описания транзакций последовательно.

    :param transactions: Список словарей с данными транзакций.
    :return: Последовательность строк с описанием каждой транзакции.
    """
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, выдающий номера банковских карт в виде формата 'XXXX XXXX XXXX XXXX'.

    :param start: Начальное значение последовательности.
    :param stop: Конечное значение последовательности.
    :return: Следующий номер банковской карты в формате 'XXXX XXXX XXXX XXXX'.
    """
    for number in range(start, stop + 1):
        formatted_card = f"{number:016d}"
        yield " ".join(formatted_card[i:i + 4] for i in range(0, len(formatted_card), 4))