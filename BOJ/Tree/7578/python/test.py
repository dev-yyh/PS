import sys
input = sys.stdin.readline

def sum(i):
	ret = 0
	while i > 0:
		ret += tree[i]
		i -= (i & -i)
	return ret

def update(i, diff):
	while i <= N:
		tree[i] += diff
		i += (i & -i)

if __name__ == '__main__':
	N = int(input())
	tree = [0] * (N+1)

	A = {}
	for idx, num in enumerate(list(map(int, input().split()))):
		A[num] = idx + 1
	B = list(map(int, input().split()))

	ans = 0
	for b in B:
		ans += (sum(N) - sum(A[b]))
		update(A[b], 1)
	
	print(ans)


	