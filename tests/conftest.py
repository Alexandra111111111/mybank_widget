from typing import Final

import pytest

# Используем финальный тип для констант
FINAL_MASK_CARD_NUMBER: Final[str] = "7000 79** **** 6361"
FINAL_MASK_ACCOUNT: Final[str] = "**4305"


@pytest.fixture
def mask_card_number() -> str:
    return FINAL_MASK_CARD_NUMBER


@pytest.fixture
def mask_account() -> str:
    return FINAL_MASK_ACCOUNT
