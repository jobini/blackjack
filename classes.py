from random import randrange

class Game:
    def __init__(self):
        self.p = Player()
        self.dealer = Dealer()
        self.beginning = True

    def deal(self):
        print "Cash:",self.p.cash
        self.p.hit()
        self.p.hit()

    def display(self):
        print 'You: {0}'.format(self.p.current_hand.cards)

    def ask_bet(self):
        try:
            bet_amount = int(raw_input("Enter bet amount for this hand: "))
        except:
            print "Enter a valid amount!"
            self.ask_bet()

        while bet_amount > self.p.cash:
            print "You don't have that much money. Try again."
            self.ask_bet()

        print "Bet amount:",bet_amount
        return bet_amount

    def ask_action(self):
        actions = ['h','s','d','p']

        act = raw_input("What will you do? (h: Hit | s: Stand | d: Double down | p: Split): ")
        while act not in actions:
            print "Invalid response! Try again."
            self.ask_action()
        return act

    def is_valid_split(self):
        if self.beginning:
            if self.p.current_hand.cards[0] == self.p.current_hand.cards[1]:
                return True
            else:
                return False
        else:
            return False


class Player:

    def __init__(self):
        self.hand_list = [Hand()]
        self.cash = 100
        self.is_stand = False
        self.current_hand = self.hand_list[0]
        self.busted = False

    def hit(self):
        new_card = Card()
        self.current_hand.cards.append(new_card.value)

    def stand(self):
        self.is_stand = True

    def double(self):
        self.current_hand.bet *= 2
        self.hit()
        self.is_stand = True

    def split(self):
        new_hand = Hand()
        new_hand.cards.append(self.current_hand.cards.pop())
        self.hand_list.append(new_hand)

    def send(self,action):
        action_dict = {'h':self.hit,'s':self.stand,'d':self.double,'p':self.split}
        action_dict[action]()

class Dealer(Player):

    def play(self):
        while (not self.busted):
            self.hit()
            if self.current_hand.score > 17:
                self.busted = True

            self.display()

    def display(self):
        print 'Dealer: {0}'.format(self.current_hand.cards)

class Hand:

    def __init__(self):
        self.bet = 0
        self.cards = []

    def score(self):
        s = 0
        for card in self.cards:
            s += card
        return s

class Card:
    suites = ['Spades','Hearts','Clubs','Diamonds']
    names = ['Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']

    def __init__(self):
        rand_suite = randrange(0,4)
        rand_val = randrange(0,13)
        self.name = "{0} of {1}".format(Card.names[rand_val],Card.suites[rand_suite])

        if rand_val <= 8:
            self.value = rand_val + 2
        else:
            self.value = 10
