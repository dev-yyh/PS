import sys
input = sys.stdin.readline

if __name__ == '__main__':
	C ,N = map(int, input().split())
	L = [list(map(int, input().split())) for _ in range(N)]
	# 적어도 C명을 늘려야 하기 때문에 고객의 수 최대 값을 더해 줌.
	dp = [float('inf') for _ in range(C+101)]

	dp[0] = 0
	for cost, customer in L:
		for i in range(customer, C+101):
			dp[i] = min(dp[i], dp[i-customer] + cost)
	
	print(min(dp[C:C+101]))