from typing import Dict
from typing import List
from typing import Union


def filter_by_state(data_list: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'
    """
    result = []
    for item in data_list:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data_list: List[Dict[str, Union[int, str]]]) -> List[Dict[str, Union[int, str]]]:
    """
    Фильтрует список словарей по значению ключа 'date'
    """
    transformat_data_list = []
    for dict in data_list:
        temp_dict = {}
        for key, value in dict.items():
            if key == "id":
                temp_dict[key] = str(value)
            else:
                temp_dict[key] = value
        transformat_data_list.append(temp_dict)
    sorted_data = sorted(transformat_data_list, key=lambda x: x["date"], reverse=True)
    return sorted_data
