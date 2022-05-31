import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
	for next in graph[cur]:
		ret[next] += ret[cur]
		dfs(next)

if __name__ == '__main__':
	n, m = map(int, input().split())
	P = list(map(int, input().split()))
	graph = [[] for _ in range(n+1)]
	for i in range(n):
		cur = i+1
		parent = P[i]
		if parent == -1:
			continue
		graph[parent].append(cur)

	ret = [0 for _ in range(n+1)]
	for _ in range(m):
		i, w = map(int, input().split())
		ret[i] += w
	
	dfs(1)
	print(*ret[1:])



