import random

cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
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

##Calculates the value of the passed hand
def calculateValue(hand):
    value = 0
    aces = 0
    ##Sum value of cards in hand, initially assuming aces = 11
    for card in hand:
        if type(card) == int:
            value += card
        elif card == "A":
            value += 11
            aces += 1
        else:
            value += 10
    ##Adjusts aces to equal 1 if hand value is greater than 21
    if value > 21 and aces > 0:
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
    return value




createDeck()
dealCards()
print(f"Your cards: {playerHand} Current Value: {calculateValue(playerHand)}")
print(f"Dealer showing: {dealerHand[0]}")