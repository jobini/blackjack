from classes import Player
from random import randrange

def new_game():
    dealer_played = False
    bet = place_bet()
    p = Player(bet)

    pc1,pc2,dc1 = deal()
    p.decks[0].append(pc1)
    p.decks[0].append(pc2)

    display(p)
    global is_stand = False
    response_dict = {'h':p.hit,'s':p.stand,'d':p.double,'sp':p.split}

    for deck in p.decks:
        while is_stand == False:
            action = ask_action()
            response_dict[action]()
            display(p)
            cardsum = p.score(deck)
            if cardsum > 21:
                print 'You lose this deck!'
                is_stand = False
                break
        if is_stand == True:
            dealer_plays()
            dealer_played = True



def display(player):
    pass

def place_bet():
    bet = int(raw_input("Place your bet amount: "))
    return bet

def deal():
    player_card1 = randrange(1,14)
    player_card2 = randrange(1,14)
    dealer_card1 = randrange(1,14)
    return player_card1,player_card2,dealer_card1

def dealer_plays():
    pass

def ask_action():
    action_set = set({'h','s','d','sp'})
    action = raw_input("Your action [Hit:'h', Stand:'s', Double:'d', Split:'sp']: ")
    while action not in action_set:
        print "Invalid action! Try again."
        action = ask_action()
    return action
