from src.masks import get_mask_card_number
from src.masks import get_mask_account

def mask_account_card(list):
    '''
Функция, которая умеет обрабатывать информацию о картах и счетах
    '''
    for i in list:
        i = i.split()
        if i[0] == 'Visa':
            print(f'Visa Platinum {get_mask_card_number(i[-1])}')
        elif i[0] == 'Maestro':
            print(f'Maestro {get_mask_card_number(i[-1])}')
        elif i[0] == 'Счет':
            print(f'Счет {get_mask_account(i[-1])}')

a = ["Visa Platinum 7000792289606361"]
b = ["Maestro 7000792289606361"]
c = ["Счет 73654108430135874305"]

vh = [
    'Maestro 1596837868705199',
'Счет 64686473678894779589',
'MasterCard 7158300734726758',
'Счет 35383033474447895560',
'Visa Classic 6831982476737658',
'Visa Platinum 8990922113665229',
'Visa Gold 5999414228426353',
'Счет 73654108430135874305'
]

mask_account_card(a)
mask_account_card(b)
mask_account_card(c)
mask_account_card(vh)