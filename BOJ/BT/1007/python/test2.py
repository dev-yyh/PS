#use BT
import sys
input = sys.stdin.readline

def dfs(start, n):
	if n == N//2:
		x1_total = 0
		y1_total = 0
		x2_total = 0
		y2_total = 0

		for i in range(N):
			if visited[i]:
				x1_total += P[i][0]
				y1_total += P[i][1]
			else:
				x2_total += P[i][0]
				y2_total += P[i][1]
		
		return ((x2_total - x1_total)**2 + (y2_total - y1_total)**2)**0.5
	
	ret = float('inf')
	for i in range(start, N):
		if not visited[i]:
			visited[i] = 1
			ret = min(ret, dfs(i, n+1))
			visited[i] = 0
	return ret

if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		N = int(input())
		P = [list(map(int, input().split())) for _ in range(N)]
		visited = [0] * (N+1)
		print(dfs(0, 0))
