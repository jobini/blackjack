from classes import Player

def new_game():
    bet = place_bet()
    p = Player(bet,0)

    update()

    action = ask_action()

def place_bet():
    bet = int(raw_input("Place your bet amount: "))
    return bet

def update():
    pass

def ask_action():
    action_set = set({'h','st','d','sp'})
    action = raw_input("Your action [Hit:'h', Stand:'st', Double:'d', Split:'sp']: ")
    while action not in action_set:
        print "Invalid action! Try again."
        action = ask_action()
    return action
