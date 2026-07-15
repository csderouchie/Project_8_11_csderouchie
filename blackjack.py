"""
Blackjack
Cedric DeRouchie
Terminal app for playing the game blackjack
No started code used
6/30/2026
"""
import random
import card
import game
from pathlib import Path
import json

def calculateValue(hand):
    """Calculates the value of the passed hand"""
    value = 0
    aces = 0
    #Sum value of cards in hand, initially assuming aces = 11
    for card in hand:
        value += card.value
        if card.name == "A":
            aces += 1
    ##Adjusts aces to equal 1 if hand value is greater than 21
    if value > 21 and aces > 0:
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
    return value

def createDeck():
    """Creates and shuffles a deck of card objects"""
    names = ["A", "K", "Q", "J", 10, 9, 8, 7, 6, 5, 4, 3, 2]
    deck = []
    for x in range(4):
        for name in names:
            if type(name) == int:
                deck.append(card.card(name, name))
            elif name == "A":
                deck.append(card.card(name, 11))
            else:
                deck.append(card.card(name, 10))
    random.shuffle(deck)
    return deck

def gameStats():
    """Prints stats at the end of the game"""
    global rounds
    global chips
    print(f"\n------------------------------------------------------------------------------------------\nGame Over Summary\nRounds played: {rounds}\nEnding Chips: {chips}\nNet chips per round: {(chips - 100) / rounds}")

def loadGame():
    while True:
        userInput = input(f"Blackjack\n1. New Game\n2. Load Game\nChoose option: ")
        if userInput == "1":
            newGame = game.game([], 100)
            return newGame
        elif userInput == "2":
            try:
                with open("save.json", "r") as f:
                    deck = []
                    data = json.load(f)
                    for savedCard in data["cards"]:
                        deck.append(card.card(savedCard["name"], savedCard["value"]))
                    newGame = game.game(deck, data["chips"])
                    return newGame
            except FileNotFoundError:
                print("Save file not found")
        else:
            print("Invalid input. Enter '1' or '2'")

def main(game):
    """Game loop"""
    while True:
        if game.bet == 0:
            game.newRound()
        print(f"Your cards: {game.displayHand(game.playerHand)} Current Value: {calculateValue(game.playerHand)}")
        print(f"Dealer showing: {game.dealerHand[0].name}")
        if len(game.playerHand) == 2:
            userInput = input(f"| Hit | Stay | Double Down |\n")
        else:
            userInput = input(f"| Hit | Stay |\n")
        if userInput.lower() == "hit" or userInput.lower() == "h":
            game = game.hit()
        elif userInput.lower() == "stay" or userInput.lower() == "s":
            game = game.stay()
        elif userInput.lower() == "double down" or userInput.lower() == "d":
            if len(game.playerHand) > 2:
                print("You can only double down on the first action of a round")
            elif game.bet > game.chips:
                print("You do not have enough chips to double down")
            else:
                game = game.doubleDown()
        else:
            print("Invalid input. Choose to 'stay', 'hit', or 'double down'")
            #Exit conditions
        if game.chips == 0 and game.bet == 0:
            break
        if game.bet == 0:
            userInput = input("Press enter to play again or press 'q' to quit ")
            if userInput.lower() == "q" or userInput.lower() == "quit":
                while True:
                    userInput = input("Would you like to save your progress? (y/n): ")
                    if userInput.lower() == "y" or userInput.lower() == "yes":
                        with open("save.json", "w") as f:
                            data = {
                                "chips": game.chips,
                                "cards": [card.__dict__ for card in game.deck]
                                }
                            json.dump(data, f, indent=4)
                        print("Save complete")
                        break
                    elif userInput.lower() == "n" or "no":
                        break
                    else:
                        print("Invalid input. Enter 'y' to save or 'n' to quit without saving")
                break

if __name__ == "__main__":
    main(loadGame())