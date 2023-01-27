
def solve(board):

    row, col = len(board), len(board[0])

    # using dfs to change all adjacent 'O' to 'P'
    def dfs(x, y):
        #Checking if x and y lies inside board and value of board at x, y is 'O'. If not we will return
        if x < 0 or x >= row or y < 0 or y >= col or board[x][y] == 'X' or board[x][y] == 'P':
            return
        board[x][y] = 'P'
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)

    # Traversing borders to check 'O'
    for i in range(row):
        if (board[i][0] == 'O'):
            dfs(i, 0)
        if (board[i][col-1] == 'O'):
            dfs(i, col-1)

    for i in range(col):
        if (board[0][i] == 'O'):
            dfs(0, i)
        if (board[row-1][i] == 'O'):
            dfs(row-1, i)

    # Traversing to change remaining 'O' to 'X' and 'P' to 'O' back again
    for i in range(row):
        for j in range(col):
            if (board[i][j] == 'O'):
                board[i][j] = 'X'
            if (board[i][j] == 'P'):
                board[i][j] = 'O'


if __name__ == '__main__':

    #starting with random board. Can take input from the user if required
    mat = [["X", "O", "X", "O", "X", "X"],
        ["X", "O", "X", "X", "O", "X"],
        ["X", "X", "X", "O", "X", "X"],
        ["O", "X", "X", "X", "X", "X"],
        ["X", "X", "X", "O", "X", "O"],
        ["O", "O", "X", "O", "O", "O"]]

    solve(mat)

    print(mat)
