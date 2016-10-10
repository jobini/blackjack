from classes import *

g = Game()

g.deal()

for i,hand in enumerate(g.p.hand_list):
    g.p.current_hand = g.p.hand_list[i]
    hand.bet = g.ask_bet()
    g.display()
    while(not g.p.busted and not g.p.is_stand):

        action = g.ask_action()
        if action == 'p':
            if g.is_valid_split():
                g.p.send(action)
                g.beginning = False
            else:
                print "Invalid split! Try again."
        else:
            g.p.send(action)

        if hand.score() > 21:
            g.p.busted = True

        g.display()

    if g.p.busted:
        print "You got busted! You lose this hand!"
        g.p.cash -= hand.bet
        print 'Cash: {0}'.format(g.p.cash)
    elif hand.score() == 21:
        print "Blackjack! You win!"
        g.p.cash += (3 * hand.bet)
        print 'Cash: {0}'.format(g.p.cash)
        break
    else:
        dealer_score = g.dealer.play()
        if dealer_score > 21 or dealer_score < hand.score:
            print "You win this hand!"
            g.p.cash += hand.bet
            print 'Cash: {0}'.format(g.p.cash)
        else:
            print "You lose this hand!"
            g.p.cash -= hand.bet
            print 'Cash: {0}'.format(g.p.cash)
