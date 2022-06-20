## Python3 Ok
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(node):
	for child in graph[node]:
		if visited[child]:
			continue
		
		visited[child] = True
		dfs(child)

		for i in range(1, 17):
			min_value = float('inf')
			for j in range(1, 17):
				if i != j:
					min_value = min(min_value , dp[child][j])
			
			dp[node][i] += min_value
	for i in range(1, 17):
		dp[node][i] += i
	
	return

if __name__ == "__main__":
	n = int(input())
	dp = [[0 for _ in range(17)] for _ in range(n+1)]
	graph = [[] for _ in range(n+1)]
	visited = [False for _ in range(n+1)]
	for i in range(n-1):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)

	visited[1] =True
	dfs(1)
	
	print(min(dp[1][1:]))