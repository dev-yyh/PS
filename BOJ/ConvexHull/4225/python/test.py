import sys
from math import ceil
input = sys.stdin.readline

def ccw2(a, b, c):
    return (b[0]-a[0]) * (c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])

def ccw(a, b, c):
	return (a[0]*b[1] + b[0]*c[1] + c[0]+a[1])-(b[0]*a[1] + c[0]*b[1] + a[0]*c[1])

def convex_hull():
	point.sort()
	lower = []
	for p in point:
		while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) < 0:
			lower.pop()
		lower.append(p)
	
	upper = []
	for p in reversed(point):
		while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) < 0:
			upper.pop()
		upper.append(p)
	
	return lower[:-1] + upper[:-1]

def dist(p1, p2, p3):
	x1, y1 = p1
	x2, y2 = p2
	x3, y3 = p3
	
	a = y2 - y1
	b = x1 - x2
	c = x2 * y1 - x1 * y2
	if (a**2 + b**2) == 0:
		return abs(x3-x1)
	else:
		return abs(a * x3 + b * y3 + c) / (a**2 + b ** 2) ** 0.5 

if __name__ == '__main__':

	case = 1
	while 1:
		n = int(input())
		if n == 0:
			break
		point = [list(map(int, input().split())) for _ in range(n)]
		hull = convex_hull()
		
		ans = float('inf')
		for i in range(len(hull)):
			p1 = hull[i-1]
			p2 = hull[i]
			ret = 0
			for j in range(len(hull)):
				p3 = hull[j]
				ret = max(ret, dist(p1, p2, p3))
			ans = min(ans, ret)
		
		ans = ceil(100 * ans) / 100
		print(f'Case {case}: {ans:.2f}')
		case += 1