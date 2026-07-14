"""
Blackjack
Cedric DeRouchie
Terminal app for playing the game blackjack
7/13/2026
"""
import card
import blackjack
import random

class game:
    def __init__(self):
        self.deck = []
        self.playerHand = []
        self.dealerHand = []
        self.chips = 100
        self.bet = 0

    def dealCards(self, hand, number):
        """Deals the passed number of cards to the passed hand"""
        i = 0
        while i < number:
            hand.append(self.deck[-1])
            self.deck.pop()
            i+=1
        return self
    
    def hit(self):
        """Adds a card to the player hand then check if they busted"""
        self.dealCards(self.playerHand, 1)
        print(f"You got a {self.playerHand[-1].name} making your total hand value {blackjack.calculateValue(self.playerHand)}")
        if blackjack.calculateValue(self.playerHand) > 21:
            self.lose()
        return self

    def splitPot(self):
        """Resolves a tie in a round"""
        print(f"Pot split, you get your {self.bet} chip bet back")
        self.chips = self.chips + self.bet
        self.bet = 0
        return self

    def lose(self):
        """Resolves losing a round"""
        print("Round lost \n------------------------------------------------------------------------------------------")
        self.bet = 0
        return self

    def win(self):
            """Resolves winning a round"""
            print(f"You won {self.bet * 2} chips! \n------------------------------------------------------------------------------------------")
            self.chips = self.chips + (self.bet * 2)
            self.bet = 0
            return self

    def compareHands(self):
        """Compares player and dealer hands to resolve a round"""
        if self.playerHand > self.dealerHand:
            self.win()
        elif self.playerHand < self.dealerHand:
            self.lose()
        else:
            self.splitPot()

    def doubleDown(self):
        """Doubles player bet, hits once, then stays"""
        print(f"Putting another {self.bet} chips in for a total bet of {self.bet * 2}")
        self.chips = self.chips - self.bet
        self.bet = self.bet * 2
        self.hit()
        if self.bet > 0:
            self.stay()
        return self

    def stay(self):
        """Reveals dealer hand then the dealer hits until their hand value is greater than 17. If the dealer did not bust hands are compared"""
        print(f"The dealer reveals a {self.dealerHand[-1]} making their current value {blackjack.calculateValue(self.dealerHand)}")
        if blackjack.calculateValue(self.dealerHand) < 17:
            self.dealerHit()
        if self.bet > 0:
            self.compareHands()
        return self

    def dealerHit(self):
        """Adds cards to the dealer's hand until it's value is greater than 16. If their hand value exceeds 21 they bust and the player wins"""
        while blackjack.calculateValue(self.dealerHand) < 17:
            self.dealCards(self.dealerHand, 1)
            print(f"The dealer hits revealing a {self.dealerHand[-1]} making their current hand value {blackjack.calculateValue(self.dealerHand)}")
            if blackjack.calculateValue(self.dealerHand) > 21:
                print("The dealer busted...")
                self.win()

    def placeBet(self):
        """Places bet for current round"""
        while self.bet == 0:
            self.bet = input(f"Current chips: {self.chips}\nPlace your bet: ")
            try:
                self.bet = int(self.bet)
            except:
                print("Invalid input. Must enter a whole number.")
                self.bet = 0
            else:
                if self.bet > self.chips:
                    print("You cannot bet more chips than you have")
                    self.bet = 0
                elif self.bet < 1:
                    print("You have to bet at least one chip")
                    self.bet = 0
                else:
                    self.chips = self.chips - self.bet
                    print(f"{self.chips} {self.bet}")

    def newRound(self):
        """Shuffles deck if needed then deals cards and calls placeBet() at the start of a round"""
        if len(self.deck) < 10:
            self.deck = blackjack.createDeck()
            print("Shuffling deck...")
        self.playerHand = []
        self.dealerHand = []
        self.dealCards(self.playerHand, 2)
        self.dealCards(self.dealerHand, 2)
        self.placeBet()
        return self
    
    def displayHand(self, hand):
        display = []
        for card in hand:
            display.append(card.name)
        return display
    
    def getBet(self):
        return self.bet