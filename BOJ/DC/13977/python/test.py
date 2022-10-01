import sys
input = sys.stdin.readline

MOD = 1000000007
def pow(a, b):
	ret = 1
	while b:
		if b%2:
			ret = ret * a % MOD
		a = a * a % MOD
		b = b >> 1
	return ret

if __name__ == '__main__':
	M = int(input())
	fac = [1] * 4000001
	for i in range(1, len(fac)):
		fac[i] = fac[i-1] * i % MOD

	for _ in range(M):
		N, K = map(int, input().split())
		a = fac[N]
		b = pow(fac[N-K]*fac[K] % MOD, MOD-2)
		
		print(a*b%MOD)
