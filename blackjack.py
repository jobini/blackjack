g = Game()

g.deal()

for hand in g.p.hands_list:
    hand.bet = g.ask_bet()

    while(not p.busted and not p.is_stand):
        g.display()
        action = g.ask_action(p)

        if g.is_valid(action):
            g.p.send(action)
        else:
            print "Invalid action! Try again."

    if p.busted:
        print "You lose!"
        p.cash -= hand.bet
    else:
        dealer_score = dealer_plays()
        if dealer_score > 21 or dealer_score < hand.score:
            print "You win!"
            p.cash += hand.bet
        else:
            print "You lose!"
            p.cash -= hand.bet
