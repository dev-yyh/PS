import sys
input = sys.stdin.readline

def upper_bound(list, target):
	l = 0
	r = len(list)
	while l < r:
		mid = (l+r)//2
		if target < list[mid]:
			r = mid
		else:
			l = mid + 1
	return l

def lower_bound(list, target):
	l = 0
	r = len(list)
	while l < r:
		mid = (l+r)//2
		if target <= list[mid]:
			r = mid
		else:
			l = mid + 1
	return l

def solve():
	cnt = 0
	for s in a_sum_list:
		diff = T - s
		lower = lower_bound(b_sum_list, diff)
		upper = upper_bound(b_sum_list, diff)
		cnt += (upper - lower)
	return cnt
if __name__ == '__main__':
	T = int(input())
	n = int(input())
	A = list(map(int, input().split()))
	m = int(input())
	B = list(map(int, input().split()))

	a_sum_list = []
	for i in range(n):
		s = 0
		for j in range(i, n):
			s += A[j]
			a_sum_list.append(s)
	
	b_sum_list = []
	for i in range(m):
		s = 0
		for j in range(i, m):
			s += B[j]
			b_sum_list.append(s)
	
	b_sum_list.sort()
	print(solve())