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

            decks.pop(card)

    for i in current_players:
        print(current_players[i]['name'], "has", current_players[i]['cards'][0], ",", current_players[i]['cards'][1])

        current_holding_cards = 2
        while current_holding_cards < 5 and current_players[i]['total_value'] < 21:
            action = input("Are you satisfied with your cards? (n/y) >> ")

            if action.upper() == "N":
                current_players[i]['cards'][current_holding_cards] = getRandomCard()
                decks.pop(current_players[i]['cards'][current_holding_cards])

                print(current_players[i]['name'], "has gotten", current_players[i]['cards'])
                current_holding_cards += 1
            else:
                break

    print("The game is over!")
    print("The winner is ->", getWinner(current_players))


def getRandomCard():
    return random.choice(list(decks.keys()))


def getWinner(players):
    current_winner = {}
    for i in range(len(players)):
        if not current_winner:
            current_winner = players[i]
            continue

        else:
            if players[i]['total_value'] > current_winner['total_value']:
                current_winner = players[i]

            elif players[i]['total_value'] == current_winner['total_value']:
                pass

    return current_winner['name']


if __name__ == "__main__":
    play()
