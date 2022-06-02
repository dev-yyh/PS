import sys
input = sys.stdin.readline

def solve(n, m):
	candy = [input().split() for _ in range(n)]
	dp = [0 for _ in range(10001)]

	m = int(m*100 + 0.5)
	for c, p in candy:
		c = int(c)
		p = int(float(p) * 100 + 0.5)
		for i in range(p, m+1):
			dp[i] = max(dp[i], dp[i-p] + c)
	
	return dp[m]

if __name__ == '__main__':
	while True:
		n, m = input().split()
		n = int(n)
		m = float(m)

		if n == 0 and m == 0.00:
			break

		print(solve(n, m))
	
