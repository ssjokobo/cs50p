# 2048 - A Python Clone

#### Video Demo: https://youtu.be/aHZ7WReiP7g

#### Description:
A personal project exploring the arts of making computer game, this project is a clone or a recreation of a legendary popular mobile app game called 2048 invented by Gabriele Cirulli. The game requires the player to swipe tiles around to keep adding the amont of numbers on those tiles multiply from 2 to 4 to 8 to 16 to 32 ... up until the most possible value at 131072. The player wins the game if they could make at least one 2048. However, the game will not necessary end, the player can keep playing until no possible move can be made. The game ends if all the tiles are fully occupied by at least a number and no possible swipe can be made.

##### Features:
This is a command line game. The game generates a 4 by 4 table decorated with ascii art by table2ascii (which is required to be installed as a library). The game will prompt for a user input to tell the game to swipe the board to a direction. If the swipe is possible, the game calculate the swipe and print a new board. If the swipe is impossible, the game let the player knows and re-prompt for a new input. Then check if the game ends or otherwise spawn one more tile with a number 2 (90% possibility) or 4 (10% possibility). The game re-prompt for a user input and the game continues.

2048 - A Python Clone has the following programmatic architecture:

1. A class of a board with the following methods:
- __init__ to generate a board object.
- game_on() to check if the game ends.
- spawn_num() to spawn a new number on a random empty tile each round.
- move_tiles(direction) to get an input as a direction to swipe, then generate a new board of a swiped board based on the input via functions outside of the class: swipe_left(board), swipe_right(board), swipe_up(board), swipe_down(board).
- get_board() to return the current board to be printed.

2. Customs function on the project file:
These are the function that execute the swipe to the four possible directions. The functions return the new swiped board. But along the way, it can detect if the player succesfully makes any 2048 (beyond tiles). If the player does, the functions print an announcement.
- swipe_left(board)
- swipe_right(board)
- swipe_up(board)
- swipe_down(board)

3. Helper functions outside on the helpers file:
- Constants, which are SIZE for size of the board, DIRECTIONS for the possible direction, and GOAL for 2048.
- print_board(), to print the current board using ascii art by table2ascii.
- print_control(), to let the player knows the control of the game.
- reduce_row(), to help swipe_left() and swipe_right() calculate.
- reduce_colume(), to help swipe_up() and swipe_down() calculate. (This function also rotates the board.)
- rotate_board, to help swipe_left() and swipe_right() calculate by re-rotate back to the supposed position.

##### Required Library:
pip install table2ascii

##### How to use:
1. Type "python project.py" on the command line.
2. Look at the board to select a move.
3. Input a move: 'a' = left, 'd' = right, 'w' = up, 's' = down.
4. Try to get 2048 to win the game.
5. If no possible move can be made, the game ends.

##### Technologies:
- Python

##### Collaborators:
This is a solo project by Sopon Suwannakit recreating a legendary game invented by Gabriele Cirulli.

##### License:
The project is finished and will be uploaded to my profile on GitHub as one of my portfolios.

##### Project Status:
Version 1.0