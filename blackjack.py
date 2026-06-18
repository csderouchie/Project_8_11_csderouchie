import random

cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
deck = []
playerHand = []
dealerHand = []
chips = 100
bet = 0

#Creates and shuffles the deck
def createDeck():
    global deck
    global cards
    i = 0
    while i < 4:
        deck += cards
        i+=1
    random.shuffle(deck)

#Deals the passed number of cards to the passed hand
def dealCards(hand, number):
    global deck
    i = 0
    while i < number:
        hand.append(deck[-1])
        deck.pop()
        i+=1

#Calculates the value of the passed hand
def calculateValue(hand):
    value = 0
    aces = 0
    #Sum value of cards in hand, initially assuming aces = 11
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

#Adds a card to the player hand then check if they busted
def hit(hand):
    global deck
    dealCards(hand, 1)
    if calculateValue(hand) > 21:
        print(f"You got a {playerHand[-1]} making your total hand value {calculateValue(hand)}")
        lose()

def stay(hand): #TODO: add dealer logic
    global deck
    global dealerHand
    dealer = calculateValue(dealerHand)
    player = calculateValue(hand)
    print(f"The dealer reveals a {dealerHand[-1]} making their current value {calculateValue(dealerHand)}")
    if player > dealer:
        win()
    elif player < dealer:
        lose()
    else:
        split()

def split():
        global bet
        global chips
        print(f"Pot split, you get your {bet} chip bet back")
        chips = chips + bet
        bet = 0

#Resolves losing a round
def lose():
    print("Round lost \n------------------------------------------------------------------------------------------")
    global bet
    bet = 0

#Resolves winning a round
def win():
        global bet
        global chips
        print(f"You won {bet * 2} chips! \n------------------------------------------------------------------------------------------")
        chips = chips + (bet * 2)
        bet = 0

createDeck()
#Game loop
while True:
    if bet == 0:
        dealCards(playerHand, 2)
        dealCards(dealerHand, 2)
    while bet == 0:
         bet = input(f"Current chips: {chips}\nPlace your bet: ")
         bet = int(bet)
         if bet > chips:
             print("You cannot bet more chips than you have")
             bet = 0
         elif bet < 1:
            print("You have to bet at least one chip")
            bet = 0
         else:
             chips = chips - bet
    print(f"Your cards: {playerHand} Current Value: {calculateValue(playerHand)}")
    print(f"Dealer showing: {dealerHand[0]}")
    userInput = input("| Hit | Stay | Double Down |\n")
    if userInput == "hit":
        hit(playerHand)
    elif userInput == "stay":
        stay(playerHand)
    else:
        break