# This is the code for creating Black Jack game using Python

# Rule_Double A - If a player has two A cards, he/she wins the game.
# Rule_Highest value - If there is a tie, the player with the highest value wins.

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
            print("There must be at least 2 player!")

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
            action = input("Hit? (n/y) >> ")

            if action.upper() == "Y":
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
    print(getWinner(current_players))


def getWinner(players):
    filtered_players = []

    for key, value in players.items():
        if value['total_value'] <= 21:
            filtered_players.append(value)

    if not filtered_players:
        return "Draw!"

    # Rule - Double A
    player_double_A = []

    for item in filtered_players:
        if rule_double_A(item['cards']):
            player_double_A.append(item)

    if player_double_A:
        print(player_double_A)
        if len(player_double_A) == 1:
            return player_double_A[0]['name'], "has won the game with Double A!"

        else:
            winner = getBetterSuit(player_double_A[0], player_double_A[1])
            return winner['name'], "has won the game with Double A!"

    # Rule - Highest value
    highest_value = max([item['total_value'] for item in filtered_players])
    player_highest_value = [item for item in filtered_players if item['total_value'] == highest_value]

    if player_highest_value:
        if len(player_highest_value) == 1:
            return (
                player_highest_value[0]['name'], "is the winner with a total of",
                player_highest_value[0]['total_value'])

        elif len(player_highest_value) == 2:
            return ("There is a tie between", [player['name'] for player in player_highest_value], "with a total of",
                    player_highest_value[0]['total_value'])


def getRandomCard():
    return random.choice(list(decks.keys()))


def getBetterSuit(player1, player2):
    # check who has spades
    if '♠️' in player1['cards']['suit']:
        return player1

    else:
        return player2


def rule_double_A(cards):
    list_of_A_cards = ['♠️_A', '♥️_A', '♣️_A', '♦️_A']
    # check if player has hold double A
    if cards[0] in list_of_A_cards and cards[1] in list_of_A_cards:
        return True
    return False


if __name__ == "__main__":
    play()
