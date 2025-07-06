import os
import json
from unittest.mock import patch, mock_open
from src.utils import read_json_file

def test_read_json_file():
    # Тестируем чтение JSON-файла
    data = [{"amount": 100, "currency": "USD"}]
    with patch('builtins.open', mock_open(read_data=json.dumps(data))):
        result = read_json_file('test.json')
        assert result == data

def test_read_json_file_empty():
    # Тестируем пустой файл
    with patch('builtins.open', mock_open(read_data='')):
        result = read_json_file('test.json')
        assert result == []