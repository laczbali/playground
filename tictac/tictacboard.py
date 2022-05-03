import sys
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

class TicTacBoard:

    def __init__(self, rows, cols, threshold=3):
        self.rows = rows
        self.cols = cols
        self.board = [[0 for x in range(cols)] for y in range(rows)]

        self.state = GameState.ACTIVE_P1_NEXT

        self.terminal_is_dirty = False
        self.terminal_clear_rowoffset = 0

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

        return self.check_if_over()

    def check_if_over(self):
        """
        Checks if the game is over. Returns True if the game is over, False otherwise.
        """
        pass

    def show(self, auto_clear=True):
        # restore cursor position
        if self.terminal_is_dirty and auto_clear:
            sys.stdout.write(f"\x1b[{self.rows + 4 + self.terminal_clear_rowoffset}A")
            sys.stdout.flush()

        self.terminal_is_dirty = True

        # print cols indexes
        print("")
        print("")
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