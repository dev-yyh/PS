import sys
input = sys.stdin.readline

def dist(x, y):
	return (x[0] - y[0])**2 + (x[1] - y[1])**2

if __name__ == '__main__':
	N = int(input())
	point = [list(map(int, input().split())) for _ in range(N)]

	ans_idx = 0
	min_v = float('inf')
	for i in range(N):
		max_v = 0
		for j in range(N):
			if i == j: continue
			max_v = max(max_v, dist(point[i], point[j]))
		
		if min_v > max_v:
			min_v = max_v
			ans_idx = i
	
	print(*point[ans_idx])


	
