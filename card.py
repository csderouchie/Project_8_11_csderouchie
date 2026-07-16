"""
Blackjack
Cedric DeRouchie
Terminal app for playing the game blackjack
7/15/2026
"""

class card:
    def __init__(self, name, value):
        """Constructor for card objects"""
        self.name = name
        self.value = value