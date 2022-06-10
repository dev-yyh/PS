import sys
input = sys.stdin.readline

def dfs(n):
	if not graph[n]:
		return 0
	if dp[n] != -1:
		return dp[n]

	child_len = []
	for child in graph[n]:
		child_len.append(dfs(child))
	child_len.sort(reverse=True)

	dp[n] = 0	
	for i in range(len(child_len)):
		dp[n] = max(dp[n], child_len[i] + (i+1))
	
	return dp[n]

if __name__ == "__main__":
	N = int(input())
	p = list(map(int, input().split()))
	graph = [[] for _ in range(N)]
	dp = [-1 for _ in range(N)]

	for i in range(N):
		if i == 0:
			continue
		graph[p[i]].append(i)
	
	print(dfs(0))
