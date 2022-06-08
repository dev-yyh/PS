import sys
input = sys.stdin.readline

if __name__ == "__main__":
	DNA = input().rstrip()
	size = len(DNA)
	dp = [[0 for _ in range(size)] for _ in range(size)]

	for length in range(1, size):
		for l in range(size-length):
			r = l + length
			if (DNA[l] == 'a' and DNA[r] == 't') or (DNA[l] == 'g' and DNA[r] == 'c'):
				dp[l][r] = dp[l+1][r-1] + 2
			
			for m in range(l, r):
				dp[l][r] = max(dp[l][r], dp[l][m] + dp[m+1][r])
	
	print(dp[0][-1])