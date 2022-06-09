import sys
input = sys.stdin.readline

if __name__ == "__main__":
	N, M, K = map(int, input().split())
	arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
	dp = [[0 for _ in range(M+1)] for _ in range(N+1)]

	for _ in range(K):
		a, b, c = map(int, input().split())
		arr[a][b] = max(arr[a][b], c)
	
	for i in range(1, N+1):
		dp[i][2] = arr[1][i] 
	
	for i in range(1, N+1):
		for cnt in range(3, M+1):
			for start in range(1, i):
				if arr[start][i] and dp[start][cnt-1]:
					dp[i][cnt] = max(dp[i][cnt], dp[start][cnt-1] + arr[start][i])
	
	print(max(dp[N]))