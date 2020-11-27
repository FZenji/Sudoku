def possible(x, y, n, board):
    if any([board[x][i] == n for i in range(9)]): return False
    if any([board[i][y] == n for i in range(9)]): return False
    if any([board[((x//3)*3)+i][((y//3)*3)+j] == n for i in range(3) for j in range(3)]): return False
    return True


def print_board(board):
    print("-"*25)
    for i in range(9):
        print("| ", end="")
        for j in range(9): print(str(board[i][j]) + " |", end=" ") if (j+1) % 3 == 0 else print(str(board[i][j]), end=" ")
        print("")
        (i+1) % 3 == 0 and print("-"*25)


def solve(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for n in range(1, 10):
                    if possible(x, y, n, board):
                        board[x][y] = n
                        solve(board)
                        board[x][y] = 0
                return
    print_board(board)
    input("More solutions?")


#solve([[5, 3, 0, 0, 7, 0, 0, 0, 0],
#       [6, 0, 0, 1, 9, 5, 0, 0, 0],
#       [0, 9, 8, 0, 0, 0, 0, 6, 0],
#       [8, 0, 0, 0, 6, 0, 0, 0, 3],
#       [4, 0, 0, 8, 0, 3, 0, 0, 1],
#       [7, 0, 0, 0, 2, 0, 0, 0, 6],
#       [0, 6, 0, 0, 0, 0, 2, 8, 0],
#       [0, 0, 0, 4, 1, 9, 0, 0, 5],
#       [0, 0, 0, 0, 8, 0, 0, 7, 9]]))
