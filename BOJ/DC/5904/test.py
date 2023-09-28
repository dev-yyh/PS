import sys
input = sys.stdin.readline


def dfs(N, s, l):
	if N > l:
		dfs(N, s+1, 2*l + (s+4))
	else:
		prev = (l - (s + 3))//2
		if N <= prev:
			dfs(N, s-1, prev)
		elif N > prev + s + 3:
			dfs(N - (prev + s + 3), s-1, prev)
		else:
			if N == 1 + prev:
				print('m')
			else:
				print('o')


if __name__ == '__main__':
	N = int(input())
	dfs(N, 0, 3)
