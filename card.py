import random
class card:
    """
    Card object representation with values and suits
    """
    #These belong to the class
    denominations = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['s','d','h','c']

    def __init__(self, denomination, suit):

        if suit.lower() not in card.suits:
            raise ValueError("This is not a suit.")

        if denomination.upper() not in card.denominations:
            raise ValueError("This is not a possible card value.")

        self.denomination = denomination.upper()
        self.suit = suit.lower()
        
    def __str__(self):
        longSuit = ""

        if self.suit == 's':
            longSuit = "spades"
        elif self.suit == 'd':
            longSuit = "diamonds"
        elif self.suit == 'h':
            longSuit = "hearts"
        elif self.suit == 'c':
            longSuit = "clubs"
        return self.denomination + " of " + longSuit

    def __eq__(self, other):
        return self.denomination == other.denomination and self.suit == other.suit

    @staticmethod
    def randomGenerate(cardsAlreadyPlayed):
        denomination = random.choice(card.denominations)
        suit = random.choice(card.suits)
        newCard = card(denomination,suit)
        if newCard in cardsAlreadyPlayed:
            newCard = card.randomGenerate(cardsAlreadyPlayed)
        return newCard




