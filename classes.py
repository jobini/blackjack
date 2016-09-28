from random import randrange

class Player:

    def __init__(self,bet,cash=100,decks=[[]]):
        self.bet = bet
        self.winnings = winnings

    def score(self,deck):
        score = sum(deck)
        return score

    def hit(self,hn):
        card = randrange(1,14)
        self.decks[hn].append(card)

    def stand(self):
        is_stand = True

    def double(self):
        self.bet *= 2

    def split(self,hn):
        decks.append([])
        decks[1][0] = decks[0][1]
        decks[0].remove(decks[0][1])

class Game:
    pass

# class Hand:
#     pass
#
# class Deck:
#     pass
