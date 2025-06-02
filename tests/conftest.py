import pytest


@pytest.fixture
def mask_card_number():
    return "7000 79** **** 6361"


@pytest.fixture()
def mask_account():
    return "**4305"
