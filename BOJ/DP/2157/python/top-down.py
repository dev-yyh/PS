import sys
input = sys.stdin.readline

def solve(cur, cnt):
	if cnt == M:
		return -float('inf')
	if cur == N:
		return 0
	
	if dp[cur][cnt] != -1:
		return dp[cur][cnt]
	
	dp[cur][cnt] = -float('inf')
	for next in range(cur+1, N+1):
		if arr[cur][next] != 0:
			dp[cur][cnt] = max(dp[cur][cnt], solve(next, cnt+1)+ arr[cur][next])
	
	return dp[cur][cnt]

if __name__ == "__main__":
	N, M, K = map(int, input().split())
	arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
	dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]

	for _ in range(K):
		a, b, c = map(int, input().split())
		arr[a][b] = max(arr[a][b], c)
	
	print(solve(1, 0))