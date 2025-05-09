from src.masks import get_mask_account
from src.masks import get_mask_card_number
from src.widget import mask_account_card
from src.widget import get_date
from src.processing import filter_by_state
from src.processing import sort_by_date

a = "Visa Platinum 7000792289606361"
b = "Maestro 7000792289606361"
c = "Счет 73654108430135874305"

vh_1 = "Maestro 1596837868705199"
vh_2 = "Счет 64686473678894779589"
vh_3 = "MasterCard 7158300734726758"
vh_4 = "Счет 35383033474447895560"
vh_5 = "Visa Classic 6831982476737658"
vh_6 = "Visa Platinum 8990922113665229"
vh_7 = "Visa Gold 5999414228426353"
vh_8 = "Счет 73654108430135874305"

my_date = "2024-03-11T02:26:18.671407"

if __name__ == "__main__":
    print(mask_account_card(a))
    print(mask_account_card(b))
    print(mask_account_card(c))
    print(mask_account_card(vh_1))
    print(mask_account_card(vh_2))
    print(mask_account_card(vh_3))
    print(mask_account_card(vh_4))
    print(mask_account_card(vh_5))
    print(mask_account_card(vh_6))
    print(mask_account_card(vh_7))
    print(mask_account_card(vh_8))
    print(get_date(my_date))
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
    print([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])

    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
    print([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
           {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
           {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
           {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
