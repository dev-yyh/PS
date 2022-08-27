import sys
from collections import deque
input = sys.stdin.readline

def solve(start):
	visited[start] = 1
	group = [start]
	next = start
	while 1:
		next = nums[next]
		if not visited[next]:
			visited[next]=1
			group.append(next)
		else:
			if next in group:
				return group.index(next)
			else:
				return len(group)

if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		n = int(input())
		nums = [0]+list(map(int, input().split()))

		ans = 0
		visited = [0] * (n+1)
		for i in range(1, n+1):
			if not visited[i]:
				ans += solve(i)
		
		print(ans)