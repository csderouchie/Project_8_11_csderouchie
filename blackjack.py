import random

cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
deck = []
playerHand = []
dealerHand = []
chips = 100
bet = 0

def createDeck():
    """Creates and shuffles the deck"""
    global deck
    global cards
    deck = []
    i = 0
    while i < 4:
        deck += cards
        i+=1
    random.shuffle(deck)

def dealCards(hand, number):
    """Deals the passed number of cards to the passed hand"""
    global deck
    i = 0
    while i < number:
        hand.append(deck[-1])
        deck.pop()
        i+=1

def calculateValue(hand):
    """Calculates the value of the passed hand"""
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

def hit(hand):
    """Adds a card to the player hand then check if they busted"""
    global deck
    dealCards(hand, 1)
    print(f"You got a {playerHand[-1]} making your total hand value {calculateValue(hand)}")
    if calculateValue(hand) > 21:
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

def splitPot():
        """Resolves a tie in a round"""
        global bet
        global chips
        print(f"Pot split, you get your {bet} chip bet back")
        chips = chips + bet
        bet = 0

def lose():
    """Resolves losing a round"""
    print("Round lost \n------------------------------------------------------------------------------------------")
    global bet
    bet = 0

def win():
        """Resolves winning a round"""
        global bet
        global chips
        print(f"You won {bet * 2} chips! \n------------------------------------------------------------------------------------------")
        chips = chips + (bet * 2)
        bet = 0

def newRound():
    """Shuffles deck if needed then deals cards and calls placeBet() at the start of a round"""
    global playerHand
    global dealerHand
    if len(deck) < 10:
        createDeck()
        print("Shuffling deck...")
    dealCards(playerHand, 2)
    dealCards(dealerHand, 2)
    placeBet()

def placeBet():
    """Places bet for current round"""
    global bet
    global chips
    while bet == 0:
        bet = input(f"Current chips: {chips}\nPlace your bet: ")
        try:
            bet = int(bet)
        except:
            print("Invalid input. Must enter a whole number.")
            bet = 0
        else:
            if bet > chips:
                print("You cannot bet more chips than you have")
                bet = 0
            elif bet < 1:
                print("You have to bet at least one chip")
                bet = 0
            else:
                chips = chips - bet

def main():
    """Game loop"""
while True:
    if bet == 0:
        newRound()
    print(f"Your cards: {playerHand} Current Value: {calculateValue(playerHand)}")
    print(f"Dealer showing: {dealerHand[0]}")
    userInput = input("| Hit | Stay | Double Down |\n")
    if userInput == "hit":
        hit(playerHand)
    elif userInput == "stay":
        stay(playerHand)
    else:
        break

if __name__ == "__main__":
    main()