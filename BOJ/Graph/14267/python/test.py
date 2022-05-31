import sys
input = sys.stdin.readline

if __name__ == '__main__':
	n, m = map(int, input().split())
	P = [0]+list(map(int, input().split()))
	ret = [0 for _ in range(n+1)]
	for _ in range(m):
		i, w = map(int, input().split())
		ret[i] += w
	
	for i in range(2, n+1):
		ret[i] += ret[P[i]]
	print(*ret[1:])


