import game_2048
import numpy as np


newGame = game_2048.Game()

newGame.board = newGame.add_tile(newGame.board)
newGame.board = newGame.add_tile(newGame.board)

while True:
    print('-----------------------')
    print(newGame.board)
    print('Score: ', newGame.score)
    currentBoard = np.copy(newGame.board)

    if newGame.check_if_game_over(newGame.board):
        print('Game Over!')
        break

    move = input('Use WASD to move: ')
    if move == 'w':
        newGame.board, newGame.score = newGame.move_up(newGame.board, newGame.score)
    elif move == 'a':
        newGame.board, newGame.score = newGame.move_left(newGame.board, newGame.score)
    elif move == 's':
        newGame.board, newGame.score = newGame.move_down(newGame.board, newGame.score)
    elif move == 'd':
        newGame.board, newGame.score = newGame.move_right(newGame.board, newGame.score)
    else:
        print('Error. Enter valid move.')

    if not np.array_equal(currentBoard, newGame.board):
        newGame.board = newGame.add_tile(newGame.board)
