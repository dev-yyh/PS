import sys
from bisect import bisect_right
input = sys.stdin.readline

def find(x):
	if parent[x] == x:
		return x
	parent[x] = find(parent[x])
	return parent[x]

def union(x, y):
	x = find(x)
	y = find(y)
	if x == y:
		return
	
	parent[x] = y
	return

if __name__ == '__main__':
	N, M, K = map(int, input().split())
	card = list(map(int, input().split()))
	card.sort()
	A = list(map(int, input().split()))
	parent = [i for i in range(N+1)]

	for a in A:
		idx = bisect_right(card, a, 0, len(card))
		idx = find(idx)
		print(card[idx])
		
		union(idx, idx+1)

