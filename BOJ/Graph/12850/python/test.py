import sys
input = sys.stdin.readline
MOD = 1000000007

def mul(arr1, arr2):
	ans = [[0 for _ in range(8)] for _ in range(8)]
	for i in range(8):
		for j in range(8):
			for k in range(8):
				ans[i][j] += (arr1[i][k] * arr2[k][j])
			ans[i][j] = ans[i][j] % MOD
	return ans

def solve(arr, n):
	if n == 1:
		return arr
	elif n % 2:
		return mul(solve(mul(arr, arr), n//2), arr)
	else:
		return solve(mul(arr, arr), n//2)

if __name__ == '__main__':
	D = int(input())
	arr = [
		[0, 1, 1, 0, 0, 0, 0, 0],
		[1, 0, 1, 1, 0, 0, 0, 0],
		[1, 1, 0, 1, 1, 0, 0, 0],
		[0, 1, 1, 0, 1, 1, 0, 0],
		[0, 0, 1, 1, 0, 1, 0, 1],
		[0, 0, 0, 1, 1, 0, 1, 0],
		[0, 0, 0, 0, 0, 1, 0, 1],
		[0, 0, 0, 0, 1, 0, 1, 0]
	]

	print(solve(arr, D)[0][0])