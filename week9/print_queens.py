def print_queens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n):
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

if __name__ == "__main__":
    Q = [1, 3, 0, 2]
    print_queens(Q)            
