import pytest
from src.processing import transformat_int_str
from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize(
    "value, expected",
    [
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            [{"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
            [{"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        ),
        (
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
            [{"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
        ),
        (
            [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
            [{"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
        ),
    ],
)
def test_transformat_int_str(value, expected):
    result = transformat_int_str(value)
    assert result == expected


@pytest.mark.parametrize(
    "data_list, state, expected",
    [
        # Случай 1: Есть совпадающие записи
        (
            [
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        # Случай 2: Нет записей с нужным статусом
        (
            [
                {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [],  # Ничего не возвращается, так как нет EXECUTED
        ),
        # Случай 3: Смешанные данные
        (
            [
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": "939719570", "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
                {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": "615064591", "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": "615064591", "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_filter_by_state(data_list, state, expected):
    result = filter_by_state(data_list, state)
    assert result == expected


# Тест сортировки по дате в порядке убывания
@pytest.mark.parametrize(
    "data_list, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        )
    ],
)
def test_sort_by_date_descending(data_list, expected):
    result = sort_by_date(data_list)
    assert result == expected


# Тест сортировки по дате в порядке возрастания
@pytest.mark.parametrize(
    "data_list, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        )
    ],
)
def test_sort_by_date_ascending(data_list, expected):
    result = sorted(data_list, key=lambda x: x["date"], reverse=False)
    assert result == expected


# Тест сортировки при одинаковых датах
@pytest.mark.parametrize(
    "data_list, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        )
    ],
)
def test_sort_by_same_dates(data_list, expected):
    result = sort_by_date(data_list)
    assert result == expected


# Тест на некорректные форматы дат
@pytest.mark.parametrize(
    "data_list",
    [
        [
            {"id": 41428829, "state": "EXECUTED", "date": "InvalidDateFormat"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]
    ],
)
def test_incorrect_date_format(data_list):
    with pytest.raises(Exception):
        sort_by_date(data_list)
