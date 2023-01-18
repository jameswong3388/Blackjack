# This is the code for creating Black Jack game using Python
import random

decks = {
    'A_Spade': {'value': 1, 'name': 'A', 'suit': 'Spade'},
    'A_Heart': {'value': 1, 'name': 'A', 'suit': 'Heart'},
    'A_Club': {'value': 1, 'name': 'A', 'suit': 'Club'},
    'A_Diamond': {'value': 1, 'name': 'A', 'suit': 'Diamond'},

    '2_Spade': {'value': 2, 'name': '2', 'suit': 'Spade'},
    '2_Heart': {'value': 2, 'name': '2', 'suit': 'Heart'},
    '2_Club': {'value': 2, 'name': '2', 'suit': 'Club'},
    '2_Diamond': {'value': 2, 'name': '2', 'suit': 'Diamond'},

    '3_Spade': {'value': 3, 'name': '3', 'suit': 'Spade'},
    '3_Heart': {'value': 3, 'name': '3', 'suit': 'Heart'},
    '3_Club': {'value': 3, 'name': '3', 'suit': 'Club'},
    '3_Diamond': {'value': 3, 'name': '3', 'suit': 'Diamond'},

    '4_Spade': {'value': 4, 'name': '4', 'suit': 'Spade'},
    '4_Heart': {'value': 4, 'name': '4', 'suit': 'Heart'},
    '4_Club': {'value': 4, 'name': '4', 'suit': 'Club'},
    '4_Diamond': {'value': 4, 'name': '4', 'suit': 'Diamond'},

    '5_Spade': {'value': 5, 'name': '5', 'suit': 'Spade'},
    '5_Heart': {'value': 5, 'name': '5', 'suit': 'Heart'},
    '5_Club': {'value': 5, 'name': '5', 'suit': 'Club'},
    '5_Diamond': {'value': 5, 'name': '5', 'suit': 'Diamond'},

    '6_Spade': {'value': 6, 'name': '6', 'suit': 'Spade'},
    '6_Heart': {'value': 6, 'name': '6', 'suit': 'Heart'},
    '6_Club': {'value': 6, 'name': '6', 'suit': 'Club'},
    '6_Diamond': {'value': 6, 'name': '6', 'suit': 'Diamond'},

    '7_Spade': {'value': 7, 'name': '7', 'suit': 'Spade'},
    '7_Heart': {'value': 7, 'name': '7', 'suit': 'Heart'},
    '7_Club': {'value': 7, 'name': '7', 'suit': 'Club'},
    '7_Diamond': {'value': 7, 'name': '7', 'suit': 'Diamond'},

    '8_Spade': {'value': 8, 'name': '8', 'suit': 'Spade'},
    '8_Heart': {'value': 8, 'name': '8', 'suit': 'Heart'},
    '8_Club': {'value': 8, 'name': '8', 'suit': 'Club'},
    '8_Diamond': {'value': '8', 'name': '8', 'suit': 'Diamond'},

    '9_Spade': {'value': 9, 'name': '9', 'suit': 'Spade'},
    '9_Heart': {'value': 9, 'name': '9', 'suit': 'Heart'},
    '9_Club': {'value': 9, 'name': '9', 'suit': 'Club'},
    '9_Diamond': {'value': 9, 'name': '9', 'suit': 'Diamond'},

    '10_Spade': {'value': 10, 'name': '10', 'suit': 'Spade'},
    '10_Heart': {'value': 10, 'name': '10', 'suit': 'Heart'},
    '10_Club': {'value': 10, 'name': '10', 'suit': 'Club'},
    '10_Diamond': {'value': 10, 'name': '10', 'suit': 'Diamond'},

    'J_Spade': {'value': 10, 'name': 'J', 'suit': 'Spade'},
    'J_Heart': {'value': 10, 'name': 'J', 'suit': 'Heart'},
    'J_Club': {'value': 10, 'name': 'J', 'suit': 'Club'},
    'J_Diamond': {'value': 10, 'name': 'J', 'suit': 'Diamond'},

    'Q_Spade': {'value': 10, 'name': 'Q', 'suit': 'Spade'},
    'Q_Heart': {'value': 10, 'name': 'Q', 'suit': 'Heart'},
    'Q_Club': {'value': 10, 'name': 'Q', 'suit': 'Club'},
    'Q_Diamond': {'value': 10, 'name': 'Q', 'suit': 'Diamond'},

    'K_Spade': {'value': 10, 'name': 'K', 'suit': 'Spade'},
    'K_Heart': {'value': 10, 'name': 'K', 'suit': 'Heart'},
    'K_Club': {'value': 10, 'name': 'K', 'suit': 'Club'},
    'K_Diamond': {'value': 10, 'name': 'K', 'suit': 'Diamond'},
}


def play():
    current_players = {}
    print("Welcome to the game of Blackjack!")
    player_count = int(input("How many players are there >> "))

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
        print(current_players[i]['name'], "has", current_players[i]['cards'][0], "and", current_players[i]['cards'][1])

        current_holding_cards = 2
        while current_holding_cards < 5 and current_players[i]['total_value'] < 21:
            action = input("Are you satisfied with your cards? (NO/YES) >> ")

            if action.upper() == "NO":
                current_players[i]['cards'][current_holding_cards] = getRandomCard()
                decks.pop(current_players[i]['cards'][current_holding_cards])

                print(current_players[i]['name'], "has gotten", current_players[i]['cards'])
                current_holding_cards += 1
            else:
                break

    print("The game is over!")
    print("The winner is", getWinner(current_players))


def getRandomCard():
    return random.choice(list(decks.keys()))


def getWinner(players):
    current_winner = {}
    for i in players:
        if current_winner.keys() == 0:
            current_winner = players[i]
        else:
            if players[i]['total_value'] > current_winner['total_value']:
                current_winner = players[i]

            elif players[i]['total_value'] == current_winner['total_value']:
                pass

    return current_winner['name']


if __name__ == "__main__":
    play()
