from connectboard import ConnectBoard

board = ConnectBoard()
board.show()

over = False
while not over:
    col = int(input("Player 1 enter a column: "))
    over = board.make_move(col, 1)

    if over:
        break

    col = int(input("Player 2 enter a column: "))
    over = board.make_move(col, -1)
