from classes import *
from defs import *


available_commands = 'easy medium hard user'.split()

def menu():
    while True:
        command = input('Input a command: > ').lower().split()
        
        if command == ['exit']:
            break

        if len(command) == 3:
            if command[0] == 'start' and command[1] in available_commands and command[2] in available_commands:
                start_game(command[1], command[2])
            else:
                print('Wrong input!')
        else:
            print('Wrong input!')


def start_game(player1, player2):
    if player1 == 'user':
        player1 = User('X')
    if player2 == 'user':
        player2 = User('O')

    if player1 == 'easy':
        player1 = Easy('X')
    if player2 == 'easy':
        player2 = Easy('O')

    if player1 == 'medium':
        player1 = Medium('X')
    if player2 == 'medium':
        player2 = Medium('O')

    if player1 == 'hard':
        player1 = Hard('X')
    if player2 == 'hard':
        player2 = Hard('O')

    game_map = [' ' for _ in range(9)]
    show_map(game_map)

    while True:
        game_map = player1.move(game_map)
        winner = game_state(game_map)
        if winner:
            if winner in ['X', 'O']:
                print(f'{winner} wins!')
                break
            if winner == 'Draw':
                print(winner)
                break
        
        game_map = player2.move(game_map)
        winner = game_state(game_map)
        if winner:
            if winner in ['X', 'O']:
                print(f'{winner} wins!')
                break
            if winner == 'Draw':
                print(winner)
                break
        


if __name__ == '__main__':
    menu()
