def show_map(game_map: list) -> None:
    print('---------')
    for i in range(3):
        print(f'| {game_map[3 * i]} {game_map[3 * i + 1]} {game_map[3 * i + 2]} |')
    print('---------')


def turn(game_map: list, x: int, sign: str, show=True) -> list:
    
    game_map[x] = sign
    if show:
        show_map(game_map)
    return game_map


def game_state(game_map: list):
    # Checking for a winner in a rows
    for i in range(3):
        row = [game_map[3 * i + j] for j in range(3)]
        if is_winner(row):
            return is_winner(row)
    
    # Checking for a winner in a coloumns
    for i in range(3):
        col = [game_map[i + j * 3] for j in range(3)]
        if is_winner(col):
            return is_winner(col)

    # Cheking for a winner in a diags
    for i in range(2):
        if i == 0:
            if is_winner([game_map[0], game_map[4], game_map[8]]):
                return is_winner([game_map[0], game_map[4], game_map[8]])
        else:
            if is_winner([game_map[2], game_map[4], game_map[6]]):
                return is_winner([game_map[2], game_map[4], game_map[6]])
    
    # Cheking for a draw
    if ' ' not in game_map:
        return 'Draw'


def is_winner(row: list):
    if row == ['X', 'X', 'X']:
        return 'X'
    if row == ['O', 'O', 'O']:
        return 'O'


def free_spots(game_map):
    return [num for num, x in enumerate(game_map) if x == ' ']


def get_winning_pos(game_map, sign):
    fs = free_spots(game_map)
    for x in fs:
        temp = game_map.copy()
        temp[x] = sign

        if game_state(temp) == sign:
            return x
