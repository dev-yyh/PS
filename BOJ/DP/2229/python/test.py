import sys
input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	score = [0]+list(map(int, input().split()))
	dp = [0 for _ in range(N+1)]

	for i in range(2, N+1):
		min_value = float('inf')
		max_value = 0
		for j in range(i, 0, -1):
			min_value = min(min_value, score[j])
			max_value = max(max_value, score[j])
			dp[i] = max(dp[i], dp[j-1] + max_value - min_value)

	print(dp[N])