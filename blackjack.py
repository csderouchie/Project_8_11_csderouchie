import random

cards = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
deck = []
def createDeck():
    global deck
    global cards
    i = 0
    while i < 4:
        deck += cards
        i+=1
    random.shuffle(deck)

createDeck()
print(deck)