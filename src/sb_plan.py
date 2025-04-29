from src.deck import Deck
import csv

class Matchup:
    name: str
    ins: dict[str, int]
    outs: dict[str, int]

    def __init__(self, name, ins, outs):
        self.name = name
        self.ins = ins
        self.outs = outs

    def __str__(self):
        ins_str = ""
        outs_str = ""

        for k,v in self.ins.items():
            ins_str += f"{v} {k}, "
        ins_str = ins_str[:-2]

        for k, v in self.outs.items():
            outs_str += f"{v} {k}, "
        outs_str = outs_str[:-2]

        return f"{self.name}/nIn: {ins_str}/nOut: {outs_str}" 

class SideboardPlan:
    deck: Deck
    matchups: list[Matchup]

    def __init__(self, deck):
        self.deck = deck
        self.matchups = []

    def add_matchup(self, name, ins, outs):
        self.matchups.append(Matchup(name, ins, outs)) 

    def add_full_matchup(self, matchup):
        self.matchups.append(matchup)

    def export(self):
        # card name, quantity in deck, matchup1, matchup2, matchup3... 
        with open('eggs.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
            spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
        pass

