import sys
input = sys.stdin.readline

if __name__ == '__main__':
	w, n = map(int, input().split())
	A = list(map(int, input().split()))
	dp = [0 for _ in range(800001)]

	flag = False
	for i in range(n-2):
		for j in range(i):
			dp[A[i]+A[j]] = 1
		
		for j in range(i+2, n):
			temp = w - A[i+1] - A[j]
			if temp < 0:
				continue
			if dp[temp]:
				flag = True
				break
		if flag:
			break
	
	if flag:
		print('YES')
	else:
		print('NO')