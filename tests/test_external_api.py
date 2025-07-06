from unittest.mock import patch
from src.external_api import convert_to_rubles

@patch('requests.get')
def test_convert_to_rubles(mock_get):
    # Тестируем конвертацию валюты
    mock_get.return_value.json.return_value = {'rates': {'RUB': 75.0}}
    transaction = {'amount': 100, 'currency': 'USD'}
    result = convert_to_rubles(transaction)
    assert result == 7500.0