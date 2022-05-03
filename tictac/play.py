from tictacboard import TicTacBoard

board = TicTacBoard(4, 5)
board.terminal_clear_rowoffset = 1
board.show()


over = False
while not over:
    col = int(input("Player 1 enter a column: "))
    over = board.make_move(col, 1)

    if over:
        break

    col = int(input("Player 2 enter a column: "))
    over = board.make_move(col, -1)