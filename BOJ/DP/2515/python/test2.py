import sys
input = sys.stdin.readline

def upper_bound(h):
	left = 0
	right = N-1

	while left < right:
		mid = (left + right)//2
		if P[mid][0] <= h:
			left = mid + 1
		else:
			right = mid
	return right

if __name__ == '__main__':
	N, S = map(int, input().split())
	P = [list(map(int, input().split())) for _ in range(N)]
	P.sort()

	dp = [0]
	for i in range(N):
		H, C = P[i]
		idx = upper_bound(H-S)
		dp.append(max(dp[i], dp[idx]+C))
	
	print(dp[N])

