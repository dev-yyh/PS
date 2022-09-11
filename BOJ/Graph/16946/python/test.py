import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, gid):
	q = deque()
	q.append((x, y))
	visited[x][y] = gid
	cnt = 1
	while q:
		x, y = q.popleft()
		for i, j in dir:
			nx = x + i
			ny = y + j
			if 0 <= nx < N and 0 <= ny < M:
				if not visited[nx][ny] and board[nx][ny] == 0:
					visited[nx][ny] = gid
					q.append((nx, ny))
					cnt += 1
	return cnt

def get_count(x, y):
	cnt = 1
	gid = set()
	for i ,j in dir:
		nx = x + i
		ny = y + j
		if 0 <= nx < N and 0 <= ny < M:
			if visited[nx][ny]:
				gid.add(visited[nx][ny])
	
	for g in gid:
		cnt += gcnt[g]
	
	return cnt % 10

if __name__ == '__main__':
	N, M = map(int, input().split())
	board = [list(map(int, input().rstrip())) for _ in range(N)]
	visited = [[0 for _ in range(M)] for _ in range(N)]
	dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

	gid = 1
	gcnt = {}
	for i in range(N):
		for j in range(M):
			if board[i][j] == 0 and not visited[i][j]:
				cnt = bfs(i, j, gid)
				gcnt[gid] = cnt
				gid += 1

	for i in range(N):
		for j in range(M):
			if board[i][j] > 0:
				board[i][j] = get_count(i, j)
	
	for b in board:
		print(''.join(map(str,b)))