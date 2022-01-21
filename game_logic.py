from BlackJack.Deck_class import Deck
from BlackJack.Player_class import Player

# init

game_on = True
dealer = Player('Dealer')
player = Player('Przemcio', 100)

while game_on:

    # a little smart move if game is still in progress
    player.hand.remove_all_cards()
    dealer.hand.remove_all_cards()

    # everytime we recreate and reshuffle deck
    deck = Deck()
    deck.shuffle_deck()
    # draw 2 cards from deck both player and dealer
    dealer.hand.add_card_from_deck(deck, 2)
    player.hand.add_card_from_deck(deck, 2)

    # without enough balance it's not possible to play
    if player.bank.balance > 10:
        # place bet before game round
        while True:
            print(f'{player.name} Your current balance is {player.bank.balance}')
            player_bet = input('Place your bet! Minimal value of bet is 10\n')
            player_bet = int(player_bet)
            if 10 < player_bet <= player.bank.balance:
                break
            else:
                print(f'{player.name} Please enter a valid amount to bet.')
                continue

        # reveal cards
        print(f'\n{dealer.name} cards:')
        dealer.hand.show_cards('dealer')
        print(f'\n{player.name} cards:')
        player.hand.show_cards()
        print(
            f'{player.name} value of cards: {player.hand.count_value_of_cards()}\n')

        # dealer.hand.show_cards() print(f'{dealer.name} value of cards (Ace favored to less than or equal to 21): {
        # dealer.hand.count_value_of_cards()}')

        # player loop card
        if player.hand.value <= 21:
            while True:
                print(f'{player.name} turn.')
                choice = input(
                    'Type: hit (you draw a card) or stand (you pass). If you stand your turn is over, if you hit u '
                    'can draw as many cards you want\n')
                if choice == 'hit':
                    print(f'{player.name} decided to draw a card!')
                    player.hand.add_card_from_deck(deck, 1)
                    player.hand.show_cards()
                    print(
                        f'{player.name} value of cards: {player.hand.count_value_of_cards()}\n')
                    if player.hand.count_value_of_cards() > 21:
                        break
                elif choice == 'stand':
                    break
                else:
                    print(f'{player.name} Wrong command. Please, type: "hit" or "stand"')

        # dealer loop
        if player.hand.value <= 21:
            while True:
                dealer.hand.count_value_of_cards()
                print(f'\n{dealer.name} cards:')
                dealer.hand.show_cards()
                print(
                    f'{dealer.name} value of cards: {dealer.hand.count_value_of_cards()}')
                if dealer.hand.value <= 16:
                    print(f'{dealer.name} decided to draw a card!')
                    dealer.hand.add_card_from_deck(deck, 1)
                    dealer.hand.show_cards()
                    print(
                        f'{dealer.name} value of cards: {dealer.hand.count_value_of_cards()}\n')
                    continue
                elif dealer.hand.value >= 17:
                    break

        # win or lose?
        player_score = abs(player.hand.value - 21)
        dealer_score = abs(dealer.hand.value - 21)
        if player.hand.value > 21:
            print(f'{player.name} lose! You lost your {player_bet} bet')
            player.bank.remove_from_balance(player_bet)
        elif player_score < dealer_score:
            print(f'{player.name} wins! You earn 150% of your bet')
            player_bet = round(player_bet * 1.5)
            player.bank.add_to_balance(player_bet)
        elif player_score > dealer_score:
            print(f'{player.name} lose! You lost your {player_bet} bet')
            player.bank.remove_from_balance(player_bet)
        else:
            print('its a draw! No one wins. If there were any bets, they back to balance')
    else:
        print(f'{player.name} You have not enough amount to bet. Come back when you get your salary.')
        break
