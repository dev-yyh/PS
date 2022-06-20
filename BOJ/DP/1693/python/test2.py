# PyPy3 Ok
import sys
import math
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(node, color):
	if dp[node][color] != -1:
		return dp[node][color]
	
	visited[node] = 1
	ret = color
	for child in graph[node]:
		if visited[child]:
			continue
		min_value = float('inf')
		for i in range(1, m):
			if i == color:
				continue
			min_value = min(min_value, dfs(child, i))
		ret += min_value
	visited[node] = 0
	dp[node][color] = ret
	return ret

if __name__ == "__main__":
	n = int(input())
	m = int(math.log2(n))+1
	dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
	graph = [[] for _ in range(n+1)]
	visited = [0 for _ in range(n+1)]

	for i in range(n-1):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)

	graph[0].append(1)
	print(dfs(0, 0))
