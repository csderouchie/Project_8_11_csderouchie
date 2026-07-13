"""
Blackjack
Cedric DeRouchie
Terminal app for playing the game blackjack
7/13/2026
"""
import random

class card:
    def __init__(self, name, value):
        self.name = name
        self.value = value