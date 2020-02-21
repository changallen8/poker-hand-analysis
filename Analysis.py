from card import card


class analysis:
    """
    Analyzes poker hands and shows odds of hitting certain hands
    """
    odds = {
        "Pair": 0,
        "Two pair": 0,
        "Three of a kind": 0,
        "Straight": 0,
        "Flush": 0,
        "Full house": 0,
        "Four of a kind": 0,
        "Straight flush": 0
    }
    
    def __init__(self, holecards):
        """
        Creates an analysis object on your current hand
        """
        self.holecards = holecards
        self.playedCards = [holecards[0], holecards[1]]

    def showOdds(self):
        """
        Shows current odds
        """
        print("Current Odds")
        for hand, probability in self.odds.items():
            print(hand + " : " + str(probability))

    def postFlop(self):
        """
        Analyze after flop
        """
        self.sortCards()
        self.showPlayedCards()
        self.checkFlush()
        self.checkFourOfAKind()
        self.checkFullHouse()
        self.checkThreeOfAKind()
        self.checkTwoPair()
        self.checkPair()

    def checkStraightFlush(self):
        return None
    def checkFourOfAKind(self):
        cards = []
        index = len(self.playedCards) - 1
        while index > 2:
            if self.playedCards[index].denomination == self.playedCards[index - 1].denomination:
                if self.playedCards[index - 1].denomination == self.playedCards[index - 2].denomination:
                    if self.playedCards[index - 2].denomination == self.playedCards[index - 3].denomination:
                        cards.append(self.playedCards[index])
                        cards.append(self.playedCards[index - 1])
                        cards.append(self.playedCards[index - 2])
                        cards.append(self.playedCards[index - 3])
                        print("You have a four of a kind")
                        return cards
            index -= 1
        return None
    def checkFullHouse(self):
        three = self.checkThreeOfAKind()
        if three is None:
            return None
        temp = self.playedCards
        for t in three:
            temp.remove(t)
        pair = self.checkPairArray(temp)
        if pair is None:
            return None
        print("You have a Full House")
        return three + pair
    def checkFlush(self):
        suitCount = {
            'd': [],
            'c': [],
            'h': [],
            's': []
        }
        index = len(self.playedCards) - 1
        while index >= 0:
            suitCount[self.playedCards[index].suit].append(self.playedCards[index])
            if len(suitCount[self.playedCards[index].suit]) == 5:
                print("You have a Flush")
                return suitCount[self.playedCards[index].suit]
            index -= 1
        return None
    def checkStraight(self):
        return None
    def checkThreeOfAKind(self):
        cards = []
        index = len(self.playedCards) - 1
        while index > 1:
            if self.playedCards[index].denomination == self.playedCards[index - 1].denomination:
                if self.playedCards[index - 1].denomination == self.playedCards[index - 2].denomination:
                    cards.append(self.playedCards[index])
                    cards.append(self.playedCards[index - 1])
                    cards.append(self.playedCards[index - 2])
                    print("You have a three of a kind")
                    return cards
            index -= 1
        return None

    
    def checkTwoPair(self):
        pairs = []
        index = len(self.playedCards) - 1
        while index > 0:
            if self.playedCards[index].denomination == self.playedCards[index - 1].denomination:
                pairs.append([self.playedCards[index], self.playedCards[index - 1]])
            if len(pairs) == 2:
                print("You have a two pair")
                return pairs
            index -= 1
        return None
    def checkPairArray(self, cards):
        index = len(cards) - 1
        while index > 0:
            if cards[index].denomination == cards[index - 1].denomination:
                #print("You have a pair")
                return [cards[index], cards[index - 1]]
            index -= 1
        return None
    def checkPair(self):
        index = len(self.playedCards) - 1
        while index > 0:
            if self.playedCards[index].denomination == self.playedCards[index - 1].denomination:
                print("You have a pair")
                return [self.playedCards[index], self.playedCards[index - 1]]
            index -= 1
        return None
    def showPlayedCards(self):
        for c in self.playedCards:
            print(c)

    def sortCards(self):
        self.playedCards.sort(key=lambda currentCard: card.denominations.index(currentCard.denomination))
    
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
            'A': 14
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


