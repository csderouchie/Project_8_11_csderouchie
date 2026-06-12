import random

cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
deck = []
playerHand = []
dealerHand = []

##Creates and shuffles the deck
def createDeck():
    global deck
    global cards
    i = 0
    while i < 4:
        deck += cards
        i+=1
    random.shuffle(deck)

##Deals two cards to the passed hand - Cannot figure out if there is a better way to do this, will maybe fix later
def dealCards():
    global deck
    global playerHand
    global dealerHand
    i = 0
    while i < 2:
        playerHand.append(deck[-1])
        deck.pop()
        dealerHand.append(deck[-1])
        deck.pop()
        i+=1

createDeck()
dealCards()
print(f"Your cards: {playerHand}")
print(f"Dealer showing: {dealerHand[0]}")
