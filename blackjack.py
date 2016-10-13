from classes import *

def main(cash=100):

    g = Game(cash)
    g.deal()

    for i,hand in enumerate(g.p.hand_list):
        g.p.reset()
        g.p.current_hand = g.p.hand_list[i]
        hand.bet = g.ask_bet()
        g.display()
        while(not g.p.busted and not g.p.is_stand):

            action = g.ask_action()
            if action == 'p':
                if g.is_valid_split():
                    g.p.send(action)
                    g.display()
                    g.beginning = False
                else:
                    print "Invalid split! Try again."
            else:
                g.p.send(action)
                g.display()
                if hand.score() == 21:
                    print "Blackjack! You win!"
                    g.p.cash += (3 * hand.bet)
                    print 'Cash: {0}'.format(g.p.cash)
                    g.is_bj = True
                    break

            if hand.score() > 21:
                g.p.busted = True

        if not g.is_bj:
            if g.p.busted:
                print "You got busted! You lose this hand!"
                g.p.cash -= hand.bet
                print 'Cash: {0}'.format(max(0,g.p.cash))
            else:
                dealer_score = g.dealer.play()
                if dealer_score > 21:
                    print "Dealer busted! You win this hand!"
                    g.p.cash += hand.bet
                    print 'Cash: {0}'.format(g.p.cash)
                elif dealer_score < hand.score():
                    print "You win this hand!"
                    g.p.cash += hand.bet
                    print 'Cash: {0}'.format(g.p.cash)
                elif dealer_score == hand.score():
                    print "Bet returned!"
                else:
                    print "You lose this hand!"
                    g.p.cash -= hand.bet
                    print 'Cash: {0}'.format(max(0,g.p.cash))

    reply = raw_input("Play again? [y]: ")
    if reply == 'y':
        if g.p.cash <= 0:
            g.p.cash = 100
        main(g.p.cash)

main()
