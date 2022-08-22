import sys
input = sys.stdin.readline

def row_check(x, n):
	for i in range(9):
		if board[x][i] == n:
			return False
	return True

def col_check(y, n):
	for i in range(9):
		if board[i][y] == n:
			return False
	return True

def s_check(x, y, n):
	nx = (x//3)*3
	ny = (y//3)*3
	for i in range(3):
		for j in range(3):
			if board[nx+i][ny+j] == n:
				return False
	return True

def dfs(dep):
	if dep >= len(zero_list):
		for b in board:
			print(*b, sep='')
		exit()
	nx, ny = zero_list[dep]

	for i in range(1, 10):
		if row_check(nx, i) and col_check(ny, i) and s_check(nx, ny, i):
			board[nx][ny] = i
			dfs(dep+1)
			board[nx][ny] = 0

if __name__ == '__main__':
	board =[list(map(int, input().rstrip())) for _ in range(9)]
	zero_list = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
	dfs(0)