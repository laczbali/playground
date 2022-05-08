import os
from enum import Enum

class GameState(Enum):
    ACTIVE_P1_NEXT = 0
    ACTIVE_P2_NEXT = 1
    END_P1 = 2
    END_P2 = 3
    END_DRAW = 4

class TerminalColors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEFAULT = '\033[0m'

class ConnectBoard:

    def __init__(self, rows=6, cols=7, threshold=4):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for x in range(cols)] for y in range(rows)]
        self.threshold = threshold

        self.state = GameState.ACTIVE_P1_NEXT

    def make_move(self, col, player, auto_show=True):
        """
        Makes the specified move.
        
        Returns True if the game is over, False otherwise. Returns None if the move is invalid.
        """
  
        # check for invalid parameters
        if col < 0 or col >= self.cols:
            return None

        if player not in [-1, 1]:
            return None

        if self.state in [GameState.END_P1, GameState.END_P2, GameState.END_DRAW]:
            return None

        if self.state == GameState.ACTIVE_P1_NEXT and player == -1:
            return None

        if self.state == GameState.ACTIVE_P2_NEXT and player == 1:
            return None

        # check which row gets the new value
        row_to_fill = -1
        for idx in range(self.rows):
            if self.board[idx][col] != 0:
                break
            row_to_fill += 1
        
        # invalid move, column is filled already
        if row_to_fill == -1:
            return None
        
        # make the move
        self.board[row_to_fill][col] = player
        self.state = GameState((self.state.value + 1) % 2)

        if auto_show:
            self.show()

        return self.check_if_over(player, row_to_fill, col)

    def check_if_over(self, player, new_row, new_col):
        """
        Checks if the game is over. Returns True if the game is over, False otherwise.
        """
        # check in vertical direction (no need to check above the new piece)
        sum = player
        for idx in range(new_row + 1, self.rows):
            cell = self.board[idx][new_col]
            if cell != player:
                break
            sum += cell
        if abs(sum) >= self.threshold:
            self.state = GameState.END_P1 if player == 1 else GameState.END_P2
            return True

        # check in horizontal direction
        sum = player
        for idx in range(new_col + 1, self.cols):
            # check right
            cell = self.board[new_row][idx]
            if cell != player:
                break
            sum += cell
        for idx in range(new_col - 1, -1, -1):
            # check left
            cell = self.board[new_row][idx]
            if cell != player:
                break
            sum += cell
        if abs(sum) >= self.threshold:
            self.state = GameState.END_P1 if player == 1 else GameState.END_P2
            return True

        # check diagonals
        sum_tl_br = player # \
        sum_bl_tr = player # /
        for idx, row in enumerate(range(new_row + 1, self.rows)):
            # check down
            cell_left = None
            cell_right = None
            if new_col + idx + 1 < self.cols:
                cell_right = self.board[row][new_col + idx + 1]
                if cell_right == player:
                    sum_tl_br += cell_right
            if new_col - idx - 1 >= 0:
                cell_left = self.board[row][new_col - idx - 1]
                if cell_left == player:
                    sum_bl_tr += cell_left
            if cell_left != player and cell_right != player:
                break
        for idx, row in enumerate(range(new_row - 1, -1, -1)):
            # check up
            cell_left = None
            cell_right = None
            if new_col + idx + 1 < self.cols:
                cell_right = self.board[row][new_col + idx + 1]
                if cell_right == player:
                    sum_bl_tr += cell_right
            if new_col - idx - 1 >= 0:
                cell_left = self.board[row][new_col - idx - 1]
                if cell_left == player:
                    sum_tl_br += cell_left
            if cell_left != player and cell_right != player:
                break
        if abs(sum_tl_br) >= self.threshold or abs(sum_bl_tr) >= self.threshold:
            self.state = GameState.END_P1 if player == 1 else GameState.END_P2
            return True

        # check for draw (no more empty cells -> rows[0] is all non 0)
        if self.board[0].count(0) == 0:
            self.state = GameState.END_DRAW
            return True

        # game is not over
        return False
        
    def reset(self):
        """
        Resets the board to the initial state
        """

        self.board = [[0 for x in range(self.cols)] for y in range(self.rows)]
        self.state = GameState.ACTIVE_P1_NEXT

    def show(self, auto_clear=True):
        # clear terminal
        if auto_clear:
            os.system('cls||clear')

        # print cols indexes
        print("  ", end="")
        for idx in range(self.cols):
            print(idx, end=" ")
        print("")

        # print values
        for idx, row in enumerate(self.board):
            print(idx, end=" ")
            for col in row:
                color = TerminalColors.BLUE
                color = TerminalColors.RED if col == -1 else color
                color = TerminalColors.GREEN if col == 1 else color
                print(f"{color}0{TerminalColors.DEFAULT}", end=" ")
            print("")

        print("")

    def as_array(self):
        """
        Returns the current board as a 1D array
        """

        board_array = []
        for row in self.board:
            board_array += row
        return board_array

    def valid_moves(self):
        """
        Returns a list of valid moves (columns)
        """

        # check which columns are empty in the first row
        valid_moves = []
        for idx, col in enumerate(self.board[0]):
            if col == 0:
                valid_moves.append(idx)

        return valid_moves