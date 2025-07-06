import os
import requests
from typing import Dict, Optional
from dotenv import load_dotenv

load_dotenv()

def convert_to_rubles(transaction: Dict) -> Optional[float]:
    """
    Конвертирует сумму транзакции в рубли. Если транзакция была в USD или EUR,
    происходит обращение к внешнему API для получения текущего курса валют.
    """
    amount = transaction.get('amount')
    currency = transaction.get('currency')

    if amount is None and currency is None:
        return None

    if currency == 'RUB':
        return amount

    api_key = os.getenv('EXCHANGE_RATES_API_KEY')
    if not api_key:
        raise ValueError("API key is not set in environment variables.")

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data: Dict = response.json()
        rate = data.get('rates', {}).get('RUB')
        if rate:
            return amount * rate
    return None