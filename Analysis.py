
class analysis:
    """
    Analyzes poker hands and shows odds of hitting certain hands
    """
    # in order, odds at indexes: 0:pair, 1:two pair, 2:set, 3:straight, 4:flush, 5:full house, 6:four of kind, 7:straight flush
    oddsarr = [0, 0, 0, 0, 0, 0, 0, 0]

    
    def __init__(self, holecards):
        """
        Creates an analysis object on your current hand
        """
        self.holecards = holecards

    def showOdds(self):
        """
        Shows current odds
        """
        print(self.oddsarr)

    @staticmethod
    def preflop(holecards):
        """
        Analyzes own cards before flop
        """
        if holecards[0].denomination == holecards[1].denomination:
            pockets = 1
        else:
            pockets = 0
        if holecards[0].suit == holecards[1].suit:
            suited = 1
        else:
            suited = 0

        switcher = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
        }
        temp = switcher[holecards[0].denomination]
        temp2 = switcher[holecards[1].denomination]
        num1 = max(temp, temp2)
        num2 = min(temp, temp2)
        # Checks if cards are connected / can make a straight or not
        gap = num1 - num2
        if (gap < 5 or gap == 12) and gap != 0:
            connected = 1
        else:
            connected = 0
        if pockets == 1:
            print("You have a pair")
            
        elif connected == 1 and suited == 1:
            print("You have suited connectors")
        elif connected == 1:
            print("You have connectors")
        elif suited == 1:
            print("You have suited cards")
        else:
            print("Bruh fold")


