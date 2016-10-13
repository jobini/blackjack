<h1><b>Blackjack - CLI</b></h1>

<h2><b>Synopsis</b></h2>

This is a command line version of the popular [Blackjack](https://en.wikipedia.org/wiki/Blackjack) game, implemented in Python.

A notable difference is that the Ace card is always treated as having value 10. Also, the cards are being drawn from an 'infinite deck'. However, should the player ever lose all of the cash, it is automatically replenished to a value of 100 in the next game.

<h2><b>Requirements</b></h2>

Python version 2.7.6+

<h2><b>Usage</b></h2>

To play the game, simply run `python blackjack.py` in the Terminal, from the directory of the extracted files.

<h2><b>To add</b></h2>

1. Implement special case for Ace cards (value of 1 vs 10)
2. Implement a `Deck` class for drawing cards
3. Improve aesthetic feel by making use of card names and better visualization.

<h2><b>License</b></h2>

Please view LICENSE for details on the usage of code in this repository.
