import random
import numpy as np


class Game:
    board = np.zeros((4, 4), dtype=int)
    score = 0

    def add_tile(self, board):
        """
        Inserts tile at random location on board.
        Tile has 90% chance of being '2', 10% chance of being '4'

        :param board: numpy array of board to add tile to

        :return board: numpy array of board with tile added
        """

        # If board is full, return board without tile added
        if not np.any(board == 0):
            return board

        # Get value of tile
        rand = random.randrange(10)
        if rand == 0:
            tile = 4
        else:
            tile = 2

        # Replace random blank tile on board with new tile value
        blank_spaces = np.argwhere(board == 0)
        rand = random.randrange(len(blank_spaces))
        rand_tile_location_x = blank_spaces[rand][0]
        rand_tile_location_y = blank_spaces[rand][1]
        board[rand_tile_location_x, rand_tile_location_y] = tile

        return board

    def move_up(self, board, score=0):
        """
        Slides tiles up.
        Two tiles with the same value combine into one tile carrying the sum of the two tiles.

        :param board: numpy array of board before moving up
        :param score: int with score before moving up

        :return board: numpy array of board after moving up
        :return score: int with score after moving up
        """

        # Rotate board counterclockwise
        board = np.rot90(board)

        board, score = self.move_left(board, score)

        # Rotate board clockwise
        board = np.rot90(board, 3)

        return board, score

    def move_down(self, board, score=0):
        """
        Slides tiles down.
        Two tiles with the same value combine into one tile carrying the sum of the two tiles.

        :param board: numpy array of board before moving down
        :param score: int with score before moving down

        :return board: numpy array of board after moving down
        :return score: int with score after moving down
        """

        # Rotate board counterclockwise
        board = np.rot90(board)

        board, score = self.move_right(board, score)

        # Rotate board clockwise
        board = np.rot90(board, 3)

        return board, score

    def move_left(self, board, score=0):
        """
        Slides tiles left.
        Two tiles with the same value combine into one tile carrying the sum of the two tiles.

        :param board: numpy array of board before moving left
        :param score: int with score before moving left

        :return board: numpy array of board after moving left
        :return score: int with score after moving left
        """

        for row_index, row in enumerate(board):
            # Shift tiles to the left
            board[row_index] = sorted(row, key=bool, reverse=True)

            # Combine tiles with the same value
            current_index = board[row_index][0]
            for i in range(1, 4):
                if current_index == board[row_index][i] and board[row_index][i] != 0:
                    board[row_index][i-1] *= 2
                    board[row_index][i] = 0
                    score += board[row_index][i-1]  # Update score
                current_index = board[row_index][i]

            # Shift tiles to the left
            board[row_index] = sorted(row, key=bool, reverse=True)

        return board, score

    def move_right(self, board, score=0):
        """
        Slides tiles right.
        Two tiles with the same value combine into one tile carrying the sum of the two tiles.

        :param board: numpy array of board before moving right
        :param score: int with score before moving right

        :return board: numpy array of board after moving right
        :return score: int with score after moving right
        """

        for row_index, row in enumerate(board):
            # Shift tiles to the right
            board[row_index] = sorted(row, key=bool, reverse=False)

            # Combine tiles with the same value
            current_index = board[row_index][3]
            for i in range(2, -1, -1):
                if current_index == board[row_index][i] and board[row_index][i] != 0:
                    board[row_index][i+1] *= 2
                    board[row_index][i] = 0
                    score += board[row_index][i+1]  # Update score
                current_index = board[row_index][i]

            # Shift tiles to the right
            board[row_index] = sorted(row, key=bool, reverse=False)

        return board, score

    def check_if_game_over(self, board):
        """
        Checks if game is over.
        If there are no empty spaces and tiles cannot be combined, game is over.

        :param board: numpy array of board to check if game over

        :return bool with game over status
        """

        # If board has empty spaces, game is not over
        if np.any(board == 0):
            return False

        # If tiles can combined horizontally, game is not over
        for row_index, row in enumerate(board):
            current_index = board[row_index][0]
            for i in range(1, 4):
                if current_index == board[row_index][i]:
                    return False
                current_index = board[row_index][i]

        # If tiles can combined vertically, game is not over
        board = np.rot90(board)
        for row_index, row in enumerate(board):
            current_index = board[row_index][0]
            for i in range(1, 4):
                if current_index == board[row_index][i]:
                    return False
                current_index = board[row_index][i]

        return True
