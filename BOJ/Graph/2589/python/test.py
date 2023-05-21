import sys
from collections import deque
input = sys.stdin.readline


dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(x, y):
	global ans
	visited = [[0] * W for _ in range(L)]
	q = deque()
	q.append((x, y, 0))
	visited[x][y] = 1

	while q:
		cx, cy, cnt = q.popleft()
		ans = max(ans, cnt)

		for d in dir:
			nx = cx + d[0]
			ny = cy + d[1]
			if 0 <= nx < L and 0 <= ny < W and M[nx][ny] == 'L' and not visited[nx][ny]:
				visited[nx][ny] = 1
				q.append((nx, ny, cnt + 1))
	return


if __name__ == '__main__':
	L, W = map(int, input().split())
	M = [input().rstrip() for _ in range(L)]
	ans = 0

	for i in range(L):
		for j in range(W):
			if 0 < i and i + 1 < L and M[i-1][j] == 'L' and M[i+1][j] == 'L':
				continue
			if 0 < j and j + 1 < W and M[i][j-1] == 'L' and M[i][j+1] == 'L':
				continue
			if M[i][j] == 'L':
				bfs(i, j)

	print(ans)
			