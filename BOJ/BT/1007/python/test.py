import sys
import itertools
input = sys.stdin.readline

if __name__ == '__main__':
	T = int(input())
	for _ in range(T):
		N = int(input())
		P = []

		x_total = 0
		y_total = 0
		for _ in range(N):
			x, y = map(int, input().split())
			x_total += x
			y_total += y
			P.append([x, y])
		
		comb = list(itertools.combinations(P, N//2))
		comb_half_len = len(comb)//2
		ans = float('inf')
		for c in comb[:comb_half_len]:
			x1_total = 0
			y1_total = 0
			for x1, y1 in c:
				x1_total += x1
				y1_total += y1
			
			x2_total = x_total - x1_total
			y2_total = y_total - y1_total
			ans = min(ans, ((x1_total - x2_total)**2+(y1_total - y2_total)**2)**0.5)
		print(ans)

