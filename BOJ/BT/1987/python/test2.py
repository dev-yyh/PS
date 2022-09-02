import sys
input = sys.stdin.readline

def solve(cx, cy, cnt):
	global ans
	ans = max(ans, cnt)
	for x, y in dir:
		nx = cx + x
		ny = cy + y
		if 0 <= nx < R and 0 <= ny < C:
			if not visited[board[nx][ny]]:
				visited[board[nx][ny]] = 1
				solve(nx, ny, cnt+1)
				visited[board[nx][ny]] = 0

if __name__ == '__main__':
	R, C = map(int, input().split())
	board = [list(map(lambda x:ord(x)-65, input().rstrip())) for _ in range(R)]
	dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	visited = [0] * 26
	
	visited[board[0][0]] = 1
	ans = 0
	solve(0,0,1)
	print(ans)