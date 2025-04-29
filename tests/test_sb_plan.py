import pytest
from src.deck import Deck
from src.sb_plan import Matchup, SideboardPlan

def test_matchup_str():
    matchup_name = "Amulet Titan"
    ins = {"Swamp": 1, "Forest": 1, "Island": 1}
    outs = {"Mountain": 1, "Plains": 1}

    matchup = Matchup(matchup_name, ins, outs)

    assert str(matchup) == "Amulet Titan/nIn: 1 Swamp, 1 Forest, 1 Island/nOut: 1 Mountain, 1 Plains"

def test_sb_plan_export():
    decklist = """1 Mountain
1 Plains

1 Swamp
1 Forest
1 Island
"""
    deck = Deck.from_list("Amulet Titan", decklist)

    matchup_name = "Amulet Titan"
    ins = {"Swamp": 1, "Forest": 1, "Island": 1}
    outs = {"Mountain": 1, "Plains": 1}
    matchup = Matchup(matchup_name, ins, outs)

    sb_plan = SideboardPlan(deck)
    sb_plan.add_full_matchup(matchup)

    sb_plan.export()