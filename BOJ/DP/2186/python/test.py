import sys
input = sys.stdin.readline

def solve(idx, n, m):
	if idx == len(key):
			return 1
	
	if dp[idx][n][m] != -1:
		return dp[idx][n][m]

	dp[idx][n][m] = 0
	for x, y in dic:
		for i in range(1, K+1):
			xx = n+x*i
			yy = m+y*i
			if 0 <= xx < N and 0 <= yy < M and board[xx][yy] == key[idx]:
				dp[idx][n][m] += solve(idx+1, xx, yy)
	
	return dp[idx][n][m]

if __name__ == '__main__':
	N, M, K = map(int, input().split())
	board = [input().rstrip() for _ in range(N)]
	key = input().rstrip()
	dic = [(0,1), (0,-1), (1,0), (-1,0)]
	dp = [[[-1 for _ in range(M+1)] for _ in range(N+1)] for _ in range(81)]

	ret = 0
	for i in range(N):
		for j in range(M):
			if board[i][j] == key[0]:
				ret += solve(1, i, j)
	
	print(ret)



