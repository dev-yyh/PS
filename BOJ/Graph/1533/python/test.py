import sys
input = sys.stdin.readline
MOD = 1000003

def mul(A, B):
	temp = [[0] * (5*N) for _ in range(5*N)]
	for i in range(5*N):
		for j in range(5*N):
			for k in range(5*N):
				temp[i][j] += (A[i][k] * B[k][j])
			temp[i][j] = temp[i][j] % MOD
	return temp

def pow(n, temp):
	if n == 1:
		return temp
	elif n % 2:
		return mul(pow(n//2, mul(temp, temp)), temp)
	else:
		return pow(n//2, mul(temp, temp))

if __name__ == '__main__':
	N, S, E, T = map(int, input().split())
	graph = [[0] * (5*N) for _ in range(5*N)]

	for i in range(N):
		for j in range(1, 5):
			graph[i*5+j][i*5+j-1] = 1
	
	for i in range(N):
		w = list(map(int, input().rstrip()))
		for j in range(N):
			if w[j] > 0:
				graph[i*5][j*5+w[j]-1] = 1

	temp = pow(T, graph)
	print(temp[(S-1)*5][(E-1)*5])