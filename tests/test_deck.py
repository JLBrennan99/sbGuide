import pytest
from src.main import Deck

# @pytest.mark.parametrize("input, expected", [("",""),("",True), ("", None), ("", False)])
# def test_equality(input,expected):
#     assert input == expected

# def test_is():
#     assert "" is None

def test_split_card_quantities():
    decklist = """1 Swamp
2 Swamp

1 Mountain
2 Mountain
"""

    deck = Deck.from_list("prowess", decklist)
    expected_main = {"Swamp": 3}
    expected_side = {"Mountain": 3}
    expected_deck = Deck("prowess", expected_main, expected_side)

    assert deck == expected_deck
    # assert deck is expected_deck
    # assert deck.name == "prowess"
    # assert deck.main == expected_main
    # assert deck.side == expected_side

def test_same_card_main_side():
    decklist = """1 Swamp
2 Mountain

1 Mountain
2 Swamp
"""

    deck = Deck.from_list("prowess", decklist)
    expected_main = {"Swamp": 1, "Mountain": 2}
    expected_side = {"Mountain": 1, "Swamp": 2}
    expected_deck = Deck("prowess", expected_main, expected_side)

    assert deck == expected_deck
    # assert deck is expected_deck
    # assert deck.name == "prowess"
    # assert deck.main == expected_main
    # assert deck.side == expected_side
