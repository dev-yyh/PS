import sys
input = sys.stdin.readline

def dfs(dep):
	if dep == M:
		print(' '.join(map(str, ans)))
		return
	
	prev = 0
	for i, n in enumerate(nums):
		if not visited[i] and prev != n:
			visited[i] = 1
			prev = n
			ans[dep] = n
			dfs(dep+1)
			visited[i] = 0

if __name__ == '__main__':
	N, M = map(int, input().split())
	nums = list(map(int, input().split()))
	nums.sort()
	ans = [0] * M
	visited = [0] * N
	dfs(0)