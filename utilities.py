import random


def print_board(game_board: [[int, ], ]) -> None:
    for row in game_board:
        print("+----+" * 4)
        print(''.join(f"|{cell if cell else '':^4}|" for cell in row))
        print("+----+" * 4)


def generate_piece(game_board: [[int, ], ], user_input=False) -> {str: int, }:

    empty_cells = [(y, x) for y, row in enumerate(game_board) for x, cell in enumerate(row) if not cell]
    if not empty_cells:
        raise Exception("Board Full")
    if user_input:
        return dict(zip(('column', 'row',  'value'), (int(i) for i in input("column,row,value:").split(','))))
    return dict(
        zip(('row', 'column', 'value'), (*random.choice(empty_cells), (2 if random.random() * 100 < 90 else 4))))
