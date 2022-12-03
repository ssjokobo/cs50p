from table2ascii import table2ascii, PresetStyle


# constants
WIDTH = 4
DIRECTIONS = ["a", "d", "w", "s"]
GOAL = 2048


def print_board(board):
    printing_board = []

    # clear zeros
    for i in range(len(board)):
        printing_board.append([])
        for j in range(len(board)):
            if board[i][j] == 0:
                printing_board[i].append("")
            else:
                printing_board[i].append(board[i][j])

    # ascii formating and printing
    output = table2ascii(
        body=printing_board,
        column_widths=[10] * 4,
        style=PresetStyle.ascii_box
    )
    print(output)


def print_control():
    print("\n'a' = left, 'd' = right, 'w' = up, 's' = down")


def reduce_column(board):
    # rotate and reduce board
    new_rotated_board = []
    for i in range(WIDTH):
        column = []
        for row in board:
            if row[i] != 0:
                column.append(row[i])
        new_rotated_board.append(column)
    return new_rotated_board


def reduce_row(board):
    # reduce board
    new_board = []
    for row in board:
        new_row = []
        # colapse zeo
        for num in row:
            if num != 0:
                new_row.append(num)
        new_board.append(new_row)
    return new_board


def rotate_board(board):
    # revert the rotation back
    new_board = []
    for i in range(WIDTH):
        row = []
        for column in board:
            row.append(column[i])
        new_board.append(row)
    return new_board