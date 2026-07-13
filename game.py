"""
Blackjack
Cedric DeRouchie
Terminal app for playing the game blackjack
7/13/2026
"""

class game:
    def __init__(self, deck, chips):
        self.deck = deck
        self.playerHand = []
        self.dealerHand = []
        self.chips = chips
        self.bet = 0