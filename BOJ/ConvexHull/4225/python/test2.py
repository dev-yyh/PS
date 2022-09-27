import sys
from functools import cmp_to_key
input = sys.stdin.readline

def ccw(a, b, c):
	return (a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (b[0]*a[1] + c[0]*b[1] + a[0]*c[1])

def compare(x, y):
	res = ccw(p0, x, y)
	if res == 0:
		return (y[1] - x[1])**2 + (y[0] - x[0])**2
	elif res > 0:
		return -1
	else:
		return 1

def convex_hull():
	S = [p0]
	for i in range(len(point)):
		while len(S) >= 2 and ccw(S[-2], S[-1], point[i]) <= 0:
			S.pop()
		S.append(point[i])
	return S

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
	global p0

	case = 1
	while 1:
		n = int(input())
		if n == 0:
			break
		point = [list(map(int, input().split())) for _ in range(n)]
		point.sort()
		p0 = point[0]
		point = point[1:]
		point.sort(key=cmp_to_key(compare))	
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
		ans =round(ans+0.005, 2)
		print(f'Case {case}: {ans:.2f}')
		case += 1