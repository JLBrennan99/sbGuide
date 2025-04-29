from collections import defaultdict

class Deck:
    min_size = 60

    def __init__(self, name: str, main: dict, side: dict):
        self.name = name
        self.main = main
        self.side = side

    def __eq__(self,other):
        return self.name == other.name and self.main == other.main and self.side == other.side

    @classmethod
    def from_list(cls, name: str, decklist: str):
        mb, sb = decklist.split("\n\n")
        
        main = defaultdict(int)
        for line in mb.splitlines():
            q, n = line.split(sep=" ", maxsplit=1)
            main[n] += int(q)

        # side = { n: q for q, n in [line.split(" ") for line in sb.splitlines()] }
        # sb_lines = [line.split(sep=" ", maxsplit=1) for line in sb.splitlines()]
        # side = {n: q for q, n in sb_lines}

        side = defaultdict(int)
        for line in sb.splitlines():
            q, n = line.split(sep=" ", maxsplit=1)
            side[n] += int(q)

        return cls(name, dict(main), dict(side))

    # hashmap mainDeck;
    # hashmap sideDeck;
    # string name;

    # public Deck(hashmap main, hashmap side, string n){
    #     this.mainDeck = main;
    #     this.sideDeck = side;
    #     this.name = n;  
    # Deck d = new Deck({},{},"titan");

# decklist = """1 Swamp
# 2 Swamp

# 1 Mountain
# 2 Mountain
# """


# deck_1 = Deck("energy", {}, {})
# deck_2 = Deck.from_list("titan", decklist)

# print(deck_2.name)
# print(deck_2.main)
# print(deck_2.side)

# print(Deck.min_size)


