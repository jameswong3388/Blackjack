# This is the code for creating Black Jack game using Python
import random

decks = {
    '♠️_A': {'value': 1, 'name': 'A', 'suit': '♠️'},
    '♥️_A': {'value': 1, 'name': 'A', 'suit': '♥️'},
    '♣️_A': {'value': 1, 'name': 'A', 'suit': '♣️'},
    '♦️_A': {'value': 1, 'name': 'A', 'suit': '♦️'},

    '♠️_2': {'value': 2, 'name': '2', 'suit': '♠️'},
    '♥️_2': {'value': 2, 'name': '2', 'suit': '♥️'},
    '♣️_2': {'value': 2, 'name': '2', 'suit': '♣️'},
    '♦️_2': {'value': 2, 'name': '2', 'suit': '♦️'},

    '♠️_3': {'value': 3, 'name': '3', 'suit': '♠️'},
    '♥️_3': {'value': 3, 'name': '3', 'suit': '♥️'},
    '♣️_3': {'value': 3, 'name': '3', 'suit': '♣️'},
    '♦️_3': {'value': 3, 'name': '3', 'suit': '♦️'},

    '♠️_4': {'value': 4, 'name': '4', 'suit': '♠️'},
    '♥️_4': {'value': 4, 'name': '4', 'suit': '♥️'},
    '♣️_4': {'value': 4, 'name': '4', 'suit': '♣️'},
    '♦️_4': {'value': 4, 'name': '4', 'suit': '♦️'},

    '♠️_5': {'value': 5, 'name': '5', 'suit': '♠️'},
    '♥️_5': {'value': 5, 'name': '5', 'suit': '♥️'},
    '♣️_5': {'value': 5, 'name': '5', 'suit': '♣️'},
    '♦️_5': {'value': 5, 'name': '5', 'suit': '♦️'},

    '♠️_6': {'value': 6, 'name': '6', 'suit': '♠️'},
    '♥️_6': {'value': 6, 'name': '6', 'suit': '♥️'},
    '♣️_6': {'value': 6, 'name': '6', 'suit': '♣️'},
    '♦️_6': {'value': 6, 'name': '6', 'suit': '♦️'},

    '♠️_7': {'value': 7, 'name': '7', 'suit': '♠️'},
    '♥️_7': {'value': 7, 'name': '7', 'suit': '♥️'},
    '♣️_7': {'value': 7, 'name': '7', 'suit': '♣️'},
    '♦️_7': {'value': 7, 'name': '7', 'suit': '♦️'},

    '♠️_8': {'value': 8, 'name': '8', 'suit': '♠️'},
    '♥️_8': {'value': 8, 'name': '8', 'suit': '♥️'},
    '♣️_8': {'value': 8, 'name': '8', 'suit': '♣️'},
    '♦️_8': {'value': 8, 'name': '8', 'suit': '♦️'},

    '♠️_9': {'value': 9, 'name': '9', 'suit': '♠️'},
    '♥️_9': {'value': 9, 'name': '9', 'suit': '♥️'},
    '♣️_9': {'value': 9, 'name': '9', 'suit': '♣️'},
    '♦️_9': {'value': 9, 'name': '9', 'suit': '♦️'},

    '♠️_10': {'value': 10, 'name': '10', 'suit': '♠️'},
    '♥️_10': {'value': 10, 'name': '10', 'suit': '♥️'},
    '♣️_10': {'value': 10, 'name': '10', 'suit': '♣️'},
    '♦️_10': {'value': 10, 'name': '10', 'suit': '♦️'},

    '♠️_J': {'value': 10, 'name': 'J', 'suit': '♠️'},
    '♥️_J': {'value': 10, 'name': 'J', 'suit': '♥️'},
    '♣️_J': {'value': 10, 'name': 'J', 'suit': '♣️'},
    '♦️_J': {'value': 10, 'name': 'J', 'suit': '♦️'},

    '♠️_Q': {'value': 10, 'name': 'Q', 'suit': '♠️'},
    '♥️_Q': {'value': 10, 'name': 'Q', 'suit': '♥️'},
    '♣️_Q': {'value': 10, 'name': 'Q', 'suit': '♣️'},
    '♦️_Q': {'value': 10, 'name': 'Q', 'suit': '♦️'},

    '♠️_K': {'value': 10, 'name': 'K', 'suit': '♠️'},
    '♥️_K': {'value': 10, 'name': 'K', 'suit': '♥️'},
    '♣️_K': {'value': 10, 'name': 'K', 'suit': '♣️'},
    '♦️_K': {'value': 10, 'name': 'K', 'suit': '♦️'},
}


def play():
    current_players = {}
    print("Welcome to the game of Blackjack!")
    while True:
        player_count = int(input("How many players are there >> "))

        if player_count < 2:
            print("There must be at least one player!")

        else:
            break

    print("")

    for i in range(player_count):
        current_players[i] = {'name': input("Enter player name: "), 'cards': {}, 'total_value': 0}

        for x in range(2):
            card = getRandomCard()
            current_players[i]['cards'][x] = card

            if decks[card]['value'] == 1:
                if current_players[i]['total_value'] + 11 > 21:
                    current_players[i]['total_value'] += 1
                else:
                    current_players[i]['total_value'] += 11

            else:
                current_players[i]['total_value'] += decks[card]['value']

            decks.pop(card)

    print("")

    for i in current_players:
        print(current_players[i]['name'], "has", [card for card in current_players[i]['cards'].values()],
              "for a total of", current_players[i]['total_value'])

        current_holding_cards = 2
        while current_holding_cards < 5 and current_players[i]['total_value'] < 21:
            action = input("Are you satisfied with your cards? (n/y) >> ")

            if action.upper() == "N":
                new_card = getRandomCard()
                current_players[i]['cards'][current_holding_cards] = new_card
                current_players[i]['total_value'] += decks[new_card]['value']

                decks.pop(current_players[i]['cards'][current_holding_cards])

                print(current_players[i]['name'], "has gotten", new_card)
                print('Updated cards:', [card for card in current_players[i]['cards'].values()], "for a total of",
                      current_players[i]['total_value'])

                current_holding_cards += 1
            else:
                print("")
                break

        print("")

    print("The game is over!")
    getWinner(current_players)


def getRandomCard():
    return random.choice(list(decks.keys()))


def getBetterSuit(player1, player2):
    # check who has spades
    if '♠️' in player1['cards'].values():
        return player1

    else:
        return player2


def getWinner(players):
    current_winner = {}
    for i in range(len(players)):
        if not current_winner:
            current_winner = players[i]
            continue

        else:
            if current_winner['total_value'] < players[i]['total_value'] <= 21:
                current_winner = players[i]

            elif players[i]['total_value'] == current_winner['total_value']:
                # if the total value is the same, check if both of them have two A cards, then the one with spades wins
                # else return draw
                if len([card for card in players[i]['cards'].values() if card == 'A']) == 2 and len(
                        [card for card in current_winner['cards'].values() if card == 'A']) == 2:
                    current_winner = getBetterSuit(players[i], current_winner)

                else:
                    return print("It's a draw!")

    return print(current_winner['name'], "has won the game!")


if __name__ == "__main__":
    play()
