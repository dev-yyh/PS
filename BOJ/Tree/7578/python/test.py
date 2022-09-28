import sys
import math
input = sys.stdin.readline

def sum(node, start, end, left, right):
	if left <= start and end <= right:
		return tree[node]
	if end < left or start > right:
		return 0

	mid = (start+end)//2
	return sum(node*2, start, mid, left, right) + sum(node*2+1, mid+1, end, left, right)

def update(node, start, end, target, diff):
	if start > target or target > end:
		return
	tree[node] += diff
	if start != end:
		mid = (start + end)//2
		update(node*2, start, mid, target, diff)
		update(node*2+1, mid+1, end, target, diff)

if __name__ == '__main__':
	N = int(input())
	tree_height = math.ceil(math.log2(N))
	tree_size = 1 << (tree_height + 1)
	tree = [0] * tree_size

	A = {}
	for idx, num in enumerate(list(map(int, input().split()))):
		A[num] = idx + 1
	B = list(map(int, input().split()))

	ans = 0
	for b in B:
		ans += sum(1, 1, N, A[b]+1, N)
		update(1, 1, N, A[b], 1)
	
	print(ans)


	