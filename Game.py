from card import card
from analysis import analysis

cardsAlreadyPlayed = []

firstCardHand = card.randomGenerate(cardsAlreadyPlayed)
cardsAlreadyPlayed.append(firstCardHand)
secondCardHand = card.randomGenerate(cardsAlreadyPlayed)
cardsAlreadyPlayed.append(secondCardHand)

myHand = (firstCardHand,secondCardHand)

print("My hand is: ")

for card in myHand:
    print(card)

communityCards = []

command = input("Hit A for hand analysis")

if command == 'A':
    analysis.preflop(myHand)


for i in range(0,3):
    shownCard = card.randomGenerate(cardsAlreadyPlayed)
    cardsAlreadyPlayed.append(shownCard)
    communityCards.append(shownCard)

print("\nThe Flop is: ")

for card in communityCards:
    print(card)

print("\nThe Turn is: ")

turnCard = card.randomGenerate(cardsAlreadyPlayed)
cardsAlreadyPlayed.append(turnCard)
communityCards.append(turnCard)

print(turnCard)

print("\nThe River is: ")

riverCard = card.randomGenerate(cardsAlreadyPlayed)
cardsAlreadyPlayed.append(riverCard)
communityCards.append(riverCard)

print(riverCard)

