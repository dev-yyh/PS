import sys
from collections import defaultdict
input = sys.stdin.readline

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
	
	d = defaultdict(int)
	for i in range(m):
		s = 0
		for j in range(i, m):
			s += B[j]
			d[s] += 1
	
	cnt = 0
	for a in a_sum_list:
		diff = T - a
		cnt += d[diff]
	
	print(cnt)
