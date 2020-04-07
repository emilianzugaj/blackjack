import random


deck_template=[]
dealer_hand=[]
player_hand=[]
card_values={}
deck=[]
deck_at_once=1

for deck_used in range(deck_at_once):
    for i in range(2,11):
        for a in range(4):
            deck_template.append(str(i))
        card_values[str(i)] = i
    for a in range(4):
        deck_template.append("Jack")
        deck_template.append("Queen")
        deck_template.append("King")
        deck_template.append("As")
    card_values["Jack"] = 10
    card_values["Queen"] = 10
    card_values["King"] = 10
    card_values["As"] = 11

def new_deck(copy_deck=deck_template):
    random.shuffle(copy_deck)
    deck_creator = copy_deck[::]
    return deck_creator

def add_card_from_deck(deck_used,hand):
    if not deck_used:
        print("new deck is in use")
        deck_used = new_deck()
    card_to_hand = deck_used.pop()
    hand.append(card_to_hand)
    return deck_used

def card_sum(hand):
    sum_value = 0
    as_count = 0
    for card in hand:
        if card == "As":
            as_count += 1
        axc = card_values[card]
        sum_value += axc
    while sum_value > 21 and as_count > 0:
        sum_value = sum_value-10
        as_count -= 1
    return sum_value

deck=new_deck(deck_template)

cash=1000
while cash>0:
    player_hand=[]
    dealer_hand=[]

    print("you've got",cash,"$")

    invalid=True
    while invalid==True:
        how_much_bet=input("how much do you want to bet\n")
        try :
            bet=int(how_much_bet)
            if  bet<0:
                print("invalid input, try again")
            elif bet>cash:
                print("you don't have that much money")
            else:
                invalid=False
        except:
            print("invalid input, try again")

    add_card_from_deck(deck, dealer_hand)
    print("dealer card hiden")

    card_dealer=1
    add_card_from_deck(deck, dealer_hand)
    print("dealer got", dealer_hand[card_dealer])
    card_dealer+=1

    card_player=0
    add_card_from_deck(deck, player_hand)
    print("you got", player_hand[card_player])
    card_player+=1

    add_card_from_deck(deck, player_hand)
    print("you got", player_hand[card_player])
    card_player+=1


    while True:
        print("total", card_sum(player_hand), "points")
        if card_sum(player_hand)==21:
            print("you got blackjack")
            break
        if card_sum(player_hand)>21:
            print("you burst")
            break
        print("you've got",card_sum(player_hand),"total")
        a = input("do you want to rise? Y/N\n")
        if card_sum(player_hand)<21:
            if a == "Y" or a == "y" or a == "yes":
                add_card_from_deck(deck,player_hand)
                print("you got", player_hand[card_player])

                card_player+=1
            elif a == "N" or a == "n" or a == "no":
                break

    print("dealer have",card_sum(dealer_hand),"total")

    while card_sum(dealer_hand)<17:
        print("dealer takes a card")
        add_card_from_deck(deck,dealer_hand)
        print("dealer got")
        for i in dealer_hand:
            print( i," ",end="")

        print("dealer have", card_sum(dealer_hand),"total")

    player=card_sum(player_hand)
    dealer=card_sum(dealer_hand)

    if player>dealer and player<=21:
        if player ==21:
            print("player wins 3:2!!!",bet)
            cash+=round(bet*(3/2))
        else:
            print("player wins!")
            cash += bet
    elif player==dealer:
        print("its a draw")
    elif player<dealer and dealer>21 and player<=21:
        print("player wins",bet)
        cash += bet
    elif player>21:
        print("dealer wins")
        cash-=bet
    else :
        print("dealer wins")
        cash-=bet
    print("====new round=========")

print("your poor!")