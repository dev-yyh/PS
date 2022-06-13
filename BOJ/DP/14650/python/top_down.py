import sys
input = sys.stdin.readline

def dfs(n, num):
	if n == N:
		if num % 3 == 0:
			return 1
		else:
			return 0
	ret = 0
	for i in [0, 1, 2]:
		if n == 1 and i == 0:
			continue
		ret += dfs(n+1, 10 * num + i)
	
	return ret

if __name__ == "__main__":
	N = int(input())

	print(dfs(0, 0))