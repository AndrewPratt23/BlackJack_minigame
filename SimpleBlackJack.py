import random

            

def play_game(buyin, bet):
    cards = shuffle()
    num_cards = len(cards)
    money = buyin
    playing = True
    while playing:
        ## Shuffle when 60% of deck is gone
        if len(cards) < (.6 * num_cards):
            cards = shuffle()
            

        ## Startup
        DD = 1
        winner = -1
        dealer = deal_cards(cards)
        player = deal_cards(cards)
        print("### Round Start ###")
        print("Exposed Dealer Card:", "["+str(dealer[0])+"]")
        print("Player Cards:", player)
        print()

        ## Player
        blackjack = False
        player_hand = check_score(player)
        if player_hand == 21:
            player_active = False
            blackjack = True
        else:
            print("Player Actions:")

        first_turn = True
        player_active = True
        while player_active:

            ## Wait for Valid Input
            valid_input = False
            while not valid_input:
                if first_turn:
                    action = input("Select an Action (1 = Hit, 2 = Stand, 3 = Double Down): ")
                    if action == "1" or action == "2" or action == "3":
                        valid_input = True
                        player_action = int(action)
                    else:
                        print("Please input a valid Action")
                else:
                    action = input("Select an Action (1 = Hit, 2 = Stand): ")
                    if action == "1" or action == "2":
                        valid_input = True
                        player_action = int(action)
                    else:
                        print("Please input a valid Action")
                    
            if player_action == 1:
                first_turn = False
                new_card = cards.pop(random.randint(0, len(cards)-1))
                print("Player Hits:", new_card)
                player.append(new_card)
                player_hand = check_score(player)
                if player_hand >= 21:
                    player_active = False
                    print("Player Hand:", player)
            elif player_action == 2:
                player_hand = check_score(player)
                print("Player Stands:", player)
                player_active = False
            elif player_action == 3:
                DD = 2
                new_card = cards.pop(random.randint(0, len(cards)-1))
                print("Player Doubles Down:", new_card)
                player.append(new_card)
                print("Player Hand:", player)
                player_hand = check_score(player)
                player_active = False
                
            print("Player Total:", player_hand)
            print()

        ## Dealer - Hits until > 16
        dealer_active = True
        print("Dealer Actions:")
        print("Dealer's hand:", dealer)
        while dealer_active:
            dealer_hand = check_score(dealer)
            if dealer_hand < 17:
                new_card = cards.pop(random.randint(0, len(cards)-1))
                print("Dealer Hits:", new_card)
                dealer.append(new_card)
            else:
                print("Dealer Stands:", dealer)
                print()
                dealer_active = False


        ## Deciding Victor
        winner = victor(player_hand, dealer_hand, blackjack)

        ## Payouts
        money = payout(winner, money, bet, DD)
        print("Chips left:", money)
        print("Cards left:", len(cards))
        print("###############")
        
        ## Continue?
        playing = p_continue(money, playing)

def victor(player_hand, dealer_hand, blackjack):
    print("###############")
    print(player_hand, "vs", dealer_hand)

    if blackjack and dealer_hand != 21:
        winner = 2
        print("Blackjack!")
    elif player_hand > 21:
        winner = 0
        print("Player Bust")
    elif dealer_hand > 21:
        winner = 1
        print("Dealer Bust")
    elif player_hand > dealer_hand:
        winner = 1
        print("Player Wins")
    elif player_hand < dealer_hand:
        winner = 0
        print("Dealer Wins")
    elif player_hand == dealer_hand:
        print("Push")
    print()
    return winner

def payout(winner, money, bet, DD):
    if winner == 0:
        money = money - bet*DD
    elif winner == 1:
        money = money + bet*DD
    elif winner == 2:
        money = int(money + (1.5 * bet))
        
    return money
    
def p_continue(money, playing):
    paused = True
    deal = input("Press 'Enter' to continue, input anything leave: ")
    paused = False
    if deal != "":
        playing = False
        print("You walked away with: $" + str(money) + "!")
    print()
    print()
    return playing
            

def deal_cards(cards):
    dcard1 = cards.pop(random.randint(0, len(cards)-1))
    dcard2 = cards.pop(random.randint(0, len(cards)-1))
    return [dcard1, dcard2]

def check_score(hand):
    points = 0
    aces = 0
    for i in hand:
        points += i
        if i == 11:
            aces += 1
    while aces > 0 and points > 21:
        aces = aces - 1
        points = points - 10
    return points

def shuffle():
    print("################")
    print("### Shuffle! ###")
    print("################")
    print()
    print()
    return [2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11,
            2,3,4,5,6,7,8,9,10,10,10,10,11]


play_game(1000, 100)
