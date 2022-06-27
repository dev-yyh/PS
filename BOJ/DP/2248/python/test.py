import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def count(n, l):
	if n == 0 or l == 0:
		return 1
	
	if dp[n][l] != -1:
		return dp[n][l]

	dp[n][l] = count(n-1, l) + count(n-1, l-1)
	return dp[n][l]

def find_ans(n, l, key):
	if n == 0:
		return ''

	value = count(n-1, l)
	if value < key:
		return '1' + find_ans(n-1, l-1, key-value)
	else:
		return '0' + find_ans(n-1, l, key)

if __name__ == '__main__':
	N, L, I = map(int, input().split())
	dp = [[-1 for _ in range(L+1)] for _ in range(N+1)]

	print(find_ans(N, L, I))
