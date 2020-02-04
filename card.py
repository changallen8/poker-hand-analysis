
class card:

    denominations = ['1','2','3','4','5','6','7','8','9','T','J','Q','K','A']

    suits = ['s','d','h','c']

    def __init__(self, denomination, suit):

        
        if suit.lower() not in card.suits:
            raise ValueError("This is not a suit.")

        if denomination.upper() not in card.denominations:
            raise ValueError("This is not a possible card value.")

        self.denomination = denomination.upper()
        self.suit = suit.lower()
        
    def toString(self):
        longSuit = ""

        if self.suit == 's':
            longSuit = "spades"
        elif self.suit == 'd':
            longSuit = "diamonds"
        elif self.suit == 'h':
            longSuit = "hearts"
        elif self.suit == 'c':
            longSuit = "clubs"
        print (self.denomination + " of " + longSuit)



