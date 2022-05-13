import sys
input = sys.stdin.readline

if __name__ == '__main__':
	N ,D = map(int, input().split())
	dist = [i for i in range(D+1)]
	graph = [list(map(int, input().split())) for _ in range(N)]
  
	for i in range(D+1):
		if i != 0:
			dist[i] = min(dist[i], dist[i-1]+1)
		
		for s, e, d in graph:
			if e <= D and s == i:
				dist[e] = min(dist[e], dist[s] + d)
	
	print(dist[D])

