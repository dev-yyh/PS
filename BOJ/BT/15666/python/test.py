import sys
input = sys.stdin.readline

def dfs(dep, start):
	if dep == M:
		print(' '.join(map(str, ans)))
		return
	
	prev = 0
	for i in range(start,N):
		if prev != nums[i]:
			prev = nums[i]
			ans[dep] = nums[i]
			dfs(dep+1, i)

if __name__ == '__main__':
	N, M = map(int, input().split())
	nums = list(map(int, input().split()))
	nums.sort()
	ans = [0] * M
	dfs(0, 0)