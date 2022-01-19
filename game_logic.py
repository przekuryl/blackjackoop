from BlackJack.Deck_class import Deck
from BlackJack.Player_class import Player

# init

game_on = True
dealer = Player('Dealer')
player = Player('Przemcio')
deck = Deck()
deck.shuffle_deck()

for card in deck.all_cards:
    print(card)

dealer.hand.add_card_from_deck(deck, 2)
player.hand.add_card_from_deck(deck, 2)
# print(dealer.hand)
# print(player.hand)

while game_on:
    # reveal cards
    print(f'\n{player.name} cards:')
    player.hand.show_cards()
    print(f'{player.name} value of cards (Ace favored to less than equal to 21): {player.hand.count_value_of_cards()}')
    print(f'\n{dealer.name} cards:')
    dealer.hand.show_cards('dealer')
    # dealer.hand.show_cards()
    # print(f'{dealer.name} value of cards (Ace favored to less than or equal to 21): {dealer.hand.count_value_of_cards()}')

    if player.hand.value > 21:
        print(f'{player.name} loses because value of his cards is more than 21')
        break

    # player loop
    while True:
        print(f'{player.name} turn.')
        choice = input(
            'Type: hit (you draw a card) or stand (you pass). If you stand your turn is over, if you hit u can draw as many cards you want\n')
        if choice == 'hit':
            print(f'{player.name} decided to draw a card!')
            player.hand.add_card_from_deck(deck, 1)
            player.hand.show_cards()
            print(
                f'{player.name} value of cards (Ace favored to less than equal to 21): {player.hand.count_value_of_cards()}')
            if player.hand.count_value_of_cards() > 21:
                break
        elif choice == 'stand':
            break
        else:
            print(f'{player.name} Wrong command. Please, type: "hit" or "stand"')

    if player.hand.value > 21:
        print(f'{player.name} loses because value of his cards is more than 21')
        break

    # dealer loop
    while True:
        dealer.hand.count_value_of_cards()
        print(f'\n{dealer.name} cards:')
        dealer.hand.show_cards()
        print(
            f'{dealer.name} value of cards (Ace favored to less than equal to 21): {dealer.hand.count_value_of_cards()}')
        if dealer.hand.value <= 16:
            print(f'{dealer.name} decided to draw a card!')
            dealer.hand.add_card_from_deck(deck, 1)
            dealer.hand.show_cards()
            print(
                f'{dealer.name} value of cards (Ace favored to less than equal to 21): {dealer.hand.count_value_of_cards()}')
            continue
        elif dealer.hand.value >= 17:
            break

    # win or lose?
    player_score = abs(player.hand.value - 21)
    dealer_score = abs(dealer.hand.value - 21)
    if player_score < dealer_score:
        print(f'{player.name} wins!')
        break
    elif player_score > dealer_score:
        print(f'{dealer.name} wins!')
        break
    else:
        print('draw!')
        break
