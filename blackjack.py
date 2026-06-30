import random

cards = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
deck = []
playerHand = []
dealerHand = []
chips = 100
bet = 0
rounds = 0

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

def stay(hand):
    """Reveals dealer hand then the dealer hits until their hand value is greater than 17. If the dealer did not bust hands are compared"""
    global dealerHand
    print(f"The dealer reveals a {dealerHand[-1]} making their current value {calculateValue(dealerHand)}")
    if calculateValue(dealerHand) < 17:
        dealerHit()
    if bet > 0:
        compareHands(hand)

def compareHands(hand):
    """Compares player and dealer hands to resolve a round"""
    global dealerHand
    dealer = calculateValue(dealerHand)
    player = calculateValue(hand)
    if player > dealer:
        win()
    elif player < dealer:
        lose()
    else:
        splitPot()

def doubleDown(hand):
    global bet
    global chips
    print(f"Putting another {bet} chips in for a total bet of {bet * 2}")
    chips = chips - bet
    bet = bet * 2
    hit(hand)
    stay(hand)

def dealerHit():
    """Adds cards to the dealer's hand until it's value is greater than 17. If their hand value exceeds 21 they bust and the player wins"""
    global dealerHand
    while calculateValue(dealerHand) < 17:
        dealCards(dealerHand, 1)
        print(f"The dealer hits revealing a {dealerHand[-1]} making their current hand value {calculateValue(dealerHand)}")
        if calculateValue(dealerHand) > 21:
            print("The dealer busted...")
            win()
    
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
    global rounds
    rounds += 1
    if len(deck) < 10:
        createDeck()
        print("Shuffling deck...")
    playerHand = []
    dealerHand = []
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

def gameStats():
    """Prints stats at the end of the game"""
    global rounds
    global chips
    print(f"\n------------------------------------------------------------------------------------------\nGame Over Summary\nRounds played: {rounds}\nEnding Chips: {chips}\nNet chips per round: {(chips - 100) / rounds}")

def main():
    """Game loop"""
    while True:
        if bet == 0:
            newRound()
        print(f"Your cards: {playerHand} Current Value: {calculateValue(playerHand)}")
        print(f"Dealer showing: {dealerHand[0]}")
        if len(playerHand) == 2:
            userInput = input(f"| Hit | Stay | Double Down |\n")
        else:
            userInput = input(f"| Hit | Stay |\n")
        if userInput.lower() == "hit" or userInput.lower() == "h":
            hit(playerHand)
        elif userInput.lower() == "stay" or userInput.lower() == "s":
            stay(playerHand)
        elif userInput.lower() == "double down" or userInput.lower() == "d":
            if len(playerHand) > 2:
                print("You can only double down on the first action of a round")
            elif bet > chips:
                print("You do not have enough chips to double down")
            else:
                doubleDown(playerHand)
        else:
            print("Invalid input. Choose to 'stay', 'hit', or 'double down'")
            #Exit conditions
        if chips == 0 and bet == 0:
            gameStats()
            break
        if bet == 0:
            userInput = input("Press enter to play again or press 'q' to quit ")
            if userInput.lower() == "q" or userInput.lower() == "quit":
                gameStats()
                break

if __name__ == "__main__":
    main()