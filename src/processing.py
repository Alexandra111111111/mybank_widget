from typing import List, Dict, Optional

def filter_by_state(data_list: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'
    """
    result = []
    for item in data_list:
        if item.get('state') == state:
            result.append(item)
    return result

def sort_by_date(data_list: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'date'
    """
    sorted_data = sorted(data_list, key=lambda x: x['date'], reverse=True)
    return sorted_data