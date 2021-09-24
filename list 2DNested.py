# Lists in lists: two-dimensional arrays
# we want to create a list of lists representing the whole chessboard
# a predefined symbol named EMPTY designates an empty field on the chessboard.
board = []
EMPTY="-"

for i in range(8): 
    row = [EMPTY for i in range(8)]
    # 1. creates a row consisting of eight elements (each of them equal to EMPTY)
    board.append(row)
    # 2. appends above row list to the board list;
    # this two processes are repeated eight times
    # to create the 'board' list consisting of 64 elements(all equal to EMPTY)
# adding all the rooks
board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK
print(board)
    
# using nested list comprehension
board1 = [[EMPTY for i in range(8)] for j in range(8)]
