from typing import Dict
from typing import List
from typing import Union


def transformat_int_str(data_dict_1: List[Dict[str, Union[int, str]]]) -> List[Dict[str, str]]:
    """
    Преобразует по id int в str
    """
    transformat_data_list = []
    for dict in data_dict_1:
        temp_dict = {}
        for key, value in dict.items():
            if key == "id":
                temp_dict[key] = str(value)
            else:
                temp_dict[key] = str(value)
        transformat_data_list.append(temp_dict)
    return transformat_data_list


def filter_by_state(data_list: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'state'
    """
    result = []
    for item in data_list:
        if item.get("state") == state:
            result.append(item)
    return result


def sort_by_date(data_dict: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Фильтрует список словарей по значению ключа 'date'
    """
    sorted_data = sorted(data_dict, key=lambda x: x["date"], reverse=True)
    return sorted_data
