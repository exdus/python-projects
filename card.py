import random
class Card (object):
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    suit_names = ["Clubs","Diamonds","Hearts","Spades"]
    rank_names = [None,"Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    def __str__(self):
        return " %s of %s " %  (Card.rank_names[self.rank],Card.suit_names[self.suit])
card1 = Card(2,11)
print card1
def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1,t2)
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range (4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self,card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
deck = Deck ()
print deck
