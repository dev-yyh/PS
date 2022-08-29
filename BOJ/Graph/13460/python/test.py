import sys
from collections import deque
from types import DynamicClassAttribute
input = sys.stdin.readline

def move(x, y, dx, dy):
	cnt = 0
	nx, ny = x, y
	while board[nx+dx][ny+dy] != '#' and board[nx][ny] != 'O':
		nx += dx
		ny += dy
		cnt += 1
	return nx, ny, cnt

def solve():
	visited = {}
	dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
	q = deque()
	q.append([R, B, 0])

	while q:
		r, b, cnt = q.popleft()
		if cnt >= 10:
			return -1
		
		for x, y in dir:
			rx, ry, rcnt = move(r[0], r[1], x, y)
			bx, by, bcnt = move(b[0], b[1], x, y)

			if board[bx][by] != 'O':
				if rx == O[0] and ry == O[1]:
					return cnt + 1
				
				if rx == bx and ry == by:
					if rcnt > bcnt:
						rx, ry = rx-x, ry-y
					else:
						bx, by = bx-x, by-y
				if (rx, ry, bx, by) in visited:
					continue
				else:
					visited[(rx, ry, bx, by)] = 1
					q.append([(rx, ry), (bx, by), cnt+1])
	return -1


if __name__ == '__main__':
	N, M = map(int, input().split())
	board = [list(map(str, input().rstrip())) for _ in range(N)]
	R = ()
	B = ()
	O = ()
	for i in range(N):
		for j in range(M):
			if board[i][j] == 'R':
				R = (i, j)
			elif board[i][j] == 'B':
				B = (i, j)
			elif board[i][j] == 'O':
				O = (i, j)
	
	print(solve())