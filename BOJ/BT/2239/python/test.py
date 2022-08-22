import sys
input = sys.stdin.readline

def add(x, y, mask, i):
    board[x][y] = i
    n_row[x] |= mask
    n_col[y] |= mask
    n_square[x//3][y//3] |= mask

def remove(x, y, mask):
    board[x][y] = 0
    n_row[x] &= ~mask
    n_col[y] &= ~mask
    n_square[x//3][y//3] &= ~mask

def dfs(depth):
    if depth >= len(zero_list):
        for b in board:
            print(*b, sep='')
        exit()
    
    x, y = zero_list[depth]
    invalid = n_row[x] | n_col[y] | n_square[x//3][y//3]

    if invalid == (1<<10)-2:
        return

    for i in range(1, 10):
        mask = 1 << i
        if not invalid & mask:
            add(x, y, mask, i)
            dfs(depth+1)
            remove(x, y, mask)

if __name__ == '__main__':
    board = [list(map(int, input().rstrip())) for _ in range(9)]
    n_row = [0] * 9
    n_col = [0] * 9
    n_square = [[0] * 3 for _ in range(3)]
    zero_list = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                zero_list.append((i, j))
            else:
                n_row[i] |= 1 << board[i][j]
                n_col[j] |= 1 << board[i][j]
                n_square[i//3][j//3] |= 1 << board[i][j]
    dfs(0)