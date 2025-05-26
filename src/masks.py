def get_mask_card_number(number_card: str) -> str:
    """
    Функция get_mask_card_number принимает на вход номер
    карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    for num in number_card:
        if num not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            raise ValueError("Номер карты должен состоять из цифр")
    if len(number_card) != 16:
        raise ValueError("Номер карты должен состоять из 16 символов")
    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_card: str) -> str:
    """
    Функция get_mask_account принимает на вход номер
    счета в виде числа и возвращает маску номера по
    правилу **XXXX
    """
    for num in number_card:
        if num not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            raise ValueError("Номер карты должен состоять из цифр")
    if len(number_card) != 20:
        raise ValueError("Номер карты должен состоять из 20 символов")
    return f"**{number_card[-4:]}"
