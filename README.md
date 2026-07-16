# Project_8_11_csderouchie

Video Demo: https://www.youtube.com/watch?v=FPaw4BkbNiM

Terminal app that simulates the game blackjack. The goal of the game is to have a higher value hand than the dealer without exceeding a total hand value of 21. A round starts with spending chips to place a bet. When you win a round, you earn chips equal to twice your bet. However, if a round is lost so is your bet. One of the dealer's cards will be revealed to you during the round where you can decide to add cards to your hand or "hit" or if you are happy with the current value of your hand you can "stay" and compare your hand with the dealer's. After hands are compared, a winner of the hand is declared and you can choose if you would like to play another hand.

----- Controls: -----

Main Menu:
1. New Game: Loads a new game with a fresh deck and 100 chips
2. Load Game: Reads data from a save.json file to load a previously saved game state

Placing a bet:
Enter a number indicating how many of your chips you wish to bet

Choices in a round:
1. "Hit" or "h": Add the top card of the deck to your current hand. If the new card makes the total value of your hand exceed 21 the round is lost.
2. "Stay" or "s": The dealer reveals their hidden card then adds cards to their hand until their hand value is greater than 17. If they dealer's hand value exceeds 21 during this, you win the round. Otherwise, hand values are compared and the higher value hand wins the round.
3. "Double Down" or "d": Doubles your bet and adds one card to your hand then compares hands with the dealer. This action can only be chosen as the first and only action in a round.

After a round:
"Quit: or "q": Exit the game and answer a yes/no prompt for if you would like to save your progress. Any other input will start the next round.