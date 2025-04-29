from src.deck import Deck
from src.sb_plan import Matchup, SideboardPlan

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