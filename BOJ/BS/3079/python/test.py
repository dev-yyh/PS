import sys
input = sys.stdin.readline


if __name__ == '__main__':
	N, M = map(int, input().split())
	T = [int(input()) for _ in range(N)]

	left = min(T)
	right = max(T) * M

	cnt = 0
	while left <= right:
		mid = (left + right) // 2
		cnt = 0
		for i in range(N):
			cnt += mid // T[i]
		
		if cnt < M:
			left = mid + 1
		else:
			right = mid - 1
	
	print(left)
