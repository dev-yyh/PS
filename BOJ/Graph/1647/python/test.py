# sort시 key가 없으면 모든 튜플에 대해 sort하기 때문에 느림
import sys
input = sys.stdin.readline

def find(x):
	if parent[x] < 0:
		return x
	return find(parent[x])

def union(x, y):
	x = find(x)
	y = find(y)
	if x == y:
		return
	if parent[x] < parent[y]:
		parent[x] += parent[y]
		parent[y] = x
	else:
		parent[y] += parent[x]
		parent[x] = y
	return

def solve():
	ans = 0
	cnt = 0
	for c, a, b in edge:
		if find(a) == find(b):
			continue
		union(a, b)
		ans += c
		cnt += 1
		if cnt == N-2:
			break
	return ans
if __name__ == '__main__':
	N, M = map(int, input().split())
	edge = []
	parent = [-1] * (N+1)
	for _ in range(M):
		a, b, c = map(int, input().split())
		edge.append((c, a, b))
	
	edge.sort(key=lambda x:x[0])
	print(solve())