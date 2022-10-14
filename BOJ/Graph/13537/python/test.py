import sys
import math
input = sys.stdin.readline

def build(node, start, end):
	if start == end:
		tree[node] = [A[start]]
		return
	
	mid = (start+end)//2
	build(node*2, start, mid)
	build(node*2+1, mid+1, end)
	tree[node] = sorted(tree[node*2]+tree[node*2+1])
	return

def upper_bound(arr, key):
	left = 0
	right = len(arr)
	while left < right:
		mid = (left + right)//2
		if arr[mid] > key:
			right = mid
		else:
			left = mid + 1
	return right

def query(node, start, end, left, right, key):
	if right < start or end < left:
		return 0

	if left <= start and end <= right:
		idx = upper_bound(tree[node], key)
		return len(tree[node]) - idx

	mid = (start + end)//2
	return query(node*2, start, mid, left, right, key) + query(node*2+1, mid+1, end, left, right, key)	

if __name__ == '__main__':
	N = int(input())
	A = list(map(int, input().split()))
	M = int(input())

	h = math.ceil(math.log2(N))
	size = 1 << (h+1)
	tree = [0] * (size)
	build(1, 0, N-1)
	
	for _ in range(M):
		i, j, k = map(int, input().split())
		print(query(1, 0, N-1, i-1, j-1, k))

