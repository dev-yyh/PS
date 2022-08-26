import sys
from collections import deque
input = sys.stdin.readline

def solve():
	visited = [[0] *(w+2) for _ in range(h+2)]
	q = deque()
	q.append((0, 0))
	visited[0][0] = 1
	ans = 0
	while q:
		cx, cy = q.popleft()
		if 'a' <= board[cx][cy] <= 'z':
			visited = [[0] *(w+2) for _ in range(h+2)]
			q = deque()
			keys.add(board[cx][cy])
			board[cx][cy] = '.'
		elif 'A' <= board[cx][cy] <= 'Z': 
			if not board[cx][cy].lower() in keys:
				continue
			else:
				board[cx][cy] = '.'
		elif board[cx][cy] == '$':
			ans += 1
			board[cx][cy] = '.'

		for x, y in dir:
			nx = cx + x
			ny = cy + y
			if 0 <= nx < h+2 and 0 <= ny < w+2 and board[nx][ny] != '*' and not visited[nx][ny]:
				visited[nx][ny] = 1
				q.append((nx, ny))
	return ans

if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		h, w = map(int, input().split())
		board = [['.']*(w+2)] + [list(map(str, '.'+input().rstrip()+'.')) for _ in range(h)] + [['.']*(w+2)]
		keys = set(map(str, input().rstrip()))
		dir = [(1,0), (-1,0), (0,1), (0,-1)]
		print(solve())