class Card:
    def __init__(self, rank, suit, value=0):
        self.rank = rank
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)

if __name_== __"main"__}:
    c1 = Card('Ace', 'Clubs', 1)
    c2 = Card('2', 'Clubs', 2)
    print(c1)
    print(c2)

print(c1)
print(c2)