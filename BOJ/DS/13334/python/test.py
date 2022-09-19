import sys
import heapq
input = sys.stdin.readline

if __name__ == '__main__':
	n = int(input())
	line = []
	for _ in range(n):
		a, b = map(int, input().split())
		line.append((min(a, b), max(a, b)))
	line.sort(key= lambda x : x[1])
	d = int(input())

	q = []
	ans = 0
	
	for s, e in line:
		if e - s <= d:
			heapq.heappush(q, s)
		else:
			continue
		
		while q:
			if e - q[0] > d:
				heapq.heappop(q)
			else:
				break
		
		ans = max(ans, len(q))
	
	print(ans)



