import sys
from helpers import print_board, print_control, reduce_column, reduce_row, rotate_board, WIDTH, DIRECTIONS, GOAL
import random


class Board():
    def __init__(self, width):
        # set board
        self.board = []
        for i in range(width):
            # set row
            self.board.append([])
            for _ in range(width):
                # set column
                self.board[i].append(0)

    def game_on(self):
        for i in range(len(self.board)):
            for j in (range(len(self.board[i]))):
                # check empty cells
                if self.board[i][j] == 0:
                    return True
                elif j < len(self.board[i]) - 1 and self.board[i][j] == self.board[i][j + 1]:
                    return True
                elif i < len(self.board) - 1 and self.board[i][j] == self.board[i + 1][j]:
                    return True
        return False

    def spawn_num(self):
        # get coordination
        x = random.randrange(4)
        y = random.randrange(4)
        while self.board[x][y] != 0:
            x = random.randrange(4)
            y = random.randrange(4)

        # get number and assign
        if random.randrange(10) < 9:
            self.board[x][y] = 2
        else:
            self.board[x][y] = 4

    def move_tiles(self, direction):
        # match the control
        match direction:
            # left
            case "a":
                self.moved_board = swipe_left(self.board)
                if self.board != self.moved_board:
                    self.board = self.moved_board
                else:
                    raise ValueError
            # right
            case "d":
                self.moved_board = swipe_right(self.board)
                if self.board != self.moved_board:
                    self.board = self.moved_board
                else:
                    raise ValueError
            # up
            case "w":
                self.moved_board = swipe_up(self.board)
                if self.board != self.moved_board:
                    self.board = self.moved_board
                else:
                    raise ValueError
            # down
            case "s":
                self.moved_board = swipe_down(self.board)
                if self.board != self.moved_board:
                    self.board = self.moved_board
                else:
                    raise ValueError

    def get_board(self):
        return self.board


def main():
    # check argv
    if len(sys.argv) != 1:
        sys.exit("Usage: python project.py")

    # setting up the board
    board = Board(WIDTH)
    board.spawn_num()
    board.spawn_num()

    # game loop
    while board.game_on():
        # prep turn
        swipe_to = ""
        print_control()
        print_board(board.get_board())

        # input
        while True:
            try:
                swipe_to = input("Input: ").lower().strip()
                print()
                if swipe_to not in DIRECTIONS:
                    print_control()
                    print_board(board.get_board())
                    print("Invalid swipe. Try again!")
                else:
                    # execute
                    board.move_tiles(swipe_to)
                    board.spawn_num()
                    break

            # when can't move
            except ValueError:
                print_control()
                print_board(board.get_board())
                match swipe_to:
                    case "a":
                        print("Can't swipe left! Pick another direction.")
                    case "d":
                        print("Can't swipe right! Pick another direction.")
                    case "w":
                        print("Can't swipe up! Pick another direction.")
                    case "s":
                        print("Can't swipe down! Pick another direction.")

    # end the game
    print_board(board.get_board())
    sys.exit("GAME OVER!")


def swipe_left(board):
    board = reduce_row(board)
    new_board = []
    for row in board:
        new_row = []
        for i in range(len(row)):
            if i < len(row) - 1 and row[i] == row[i + 1]:
                new_cell = row[i] + row[i + 1]
                # catch milestones
                if new_cell >= GOAL:
                    print(f"=========--->>> YOU GOT {str(new_cell)}! <<<---=========")
                new_row.append(new_cell)
                # clear next item
                row[i + 1] = 0
            elif row[i] == 0:
                continue
            else:
                new_row.append(row[i])
        new_board.append(new_row)

    # zero fills
    for row in new_board:
        while len(row) < WIDTH:
            row.append(0)
    return new_board


def swipe_right(board):
    board = reduce_row(board)
    new_board = []
    for row in board:
        new_row = []
        for i in range(-1, - 1 - len(row), -1):
            if i > -len(row) and row[i] == row[i - 1]:
                new_cell = row[i] + row[i - 1]
                # catch milestones
                if new_cell >= GOAL:
                    print(f"=========--->>> YOU GOT {str(new_cell)}! <<<---=========")
                new_row.insert(0, new_cell)
                # clear next item
                row[i - 1] = 0
            elif row[i] == 0:
                continue
            else:
                new_row.insert(0, row[i])
        new_board.append(new_row)

    # zero fills
    for row in new_board:
        while len(row) < WIDTH:
            row.insert(0, 0)
    return new_board


def swipe_up(board):
    rotated_board = reduce_column(board)
    new_board = []
    for column in rotated_board:
        new_column = []
        for i in range(len(column)):
            if i < len(column) - 1 and column[i] == column[i + 1]:
                new_cell = column[i] + column[i + 1]
                # catch milestones
                if new_cell >= GOAL:
                    print(f"=========--->>> YOU GOT {str(new_cell)}! <<<---=========")
                new_column.append(new_cell)
                # clear next item
                column[i + 1] = 0
            elif column[i] == 0:
                continue
            else:
                new_column.append(column[i])
        new_board.append(new_column)

    # zero fills
    for row in new_board:
        while len(row) < WIDTH:
            row.append(0)

    return rotate_board(new_board)


def swipe_down(board):
    rotated_board = reduce_column(board)
    new_board = []
    for column in rotated_board:
        new_column = []
        for i in range(-1, - 1 - len(column), -1):
            if i > -len(column) and column[i] == column[i - 1]:
                new_cell = column[i] + column[i - 1]
                # catch milestones
                if new_cell >= GOAL:
                    print(f"=========--->>> YOU GOT {str(new_cell)}! <<<---=========")
                new_column.insert(0, new_cell)
                # clear next item
                column[i - 1] = 0
            elif column[i] == 0:
                continue
            else:
                new_column.insert(0, column[i])
        new_board.append(new_column)

    # zero fills
    for row in new_board:
        while len(row) < WIDTH:
            row.insert(0, 0)

    return rotate_board(new_board)


if __name__ == "__main__":
    main()