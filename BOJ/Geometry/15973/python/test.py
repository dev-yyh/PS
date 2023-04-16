import sys
input = sys.stdin.readline


def inter(a, b):
	if a[0] > b[0]:
		a, b = b, a
	
	if a[1] < b[0]:
		return 0
	elif a[1] == b[0]:
		return 1
	else:
		return 2


if __name__ == '__main__':
	P = list(map(int, input().split()))
	Q = list(map(int, input().split()))

	ix = inter((P[0], P[2]), (Q[0], Q[2]))
	iy = inter((P[1], P[3]), (Q[1], Q[3]))

	if ix == 2 and iy == 2:
		print('FACE')
	elif (ix == 1 and iy == 2) or (ix == 2 and iy == 1):
		print('LINE')
	elif ix == 1 and iy == 1:
		print('POINT')
	else:
		print('NULL')