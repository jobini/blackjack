from random import randrange

class Player:

    def __init__(self):
        self.hand_list = [Hand()]
        self.cash = 100
        self.current_hand = 0
        self.is_stand = False
        self.current_hand = self.hand_list[0]
        self.busted = False

    def hit(self):
        new_card = Card()
        self.current_hand.append(new_card.value)

    def stand(self):
        self.is_stand = True

    def double(self):
        self.current_hand.bet *= 2
        hit()
        self.is_stand = True

    def split(self,hn):
        new_hand = Hand()
        new_hand.cards.append(self.current_hand.cards.pop()])
        self.hand_list.append(new_hand)


class Game:
    pass

class Hand:
    pass

class Deck:
    pass
