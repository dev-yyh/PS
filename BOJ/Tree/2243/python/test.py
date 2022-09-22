import sys
import math
input = sys.stdin.readline
MAX = 1000000

def query(node, start, end, target):
	if start == end:
		return start
	mid = (start + end)//2
	if target <= tree[node*2]:
		return query(node*2, start, mid, target)
	else:
		return query(node*2+1, mid+1, end, target-tree[node*2])

def update(node, start, end, target, diff):
	if target < start or target > end:
		return
	
	tree[node] += diff
	if start != end:
		update(node*2, start, (start+end)//2, target, diff)
		update(node*2+1, (start+end)//2+1, end, target, diff)

if __name__ == '__main__':
	n = int(input())
	tree_height = int(math.log2(MAX)+1)
	tree_size = 1 << (tree_height+1)
	tree =[0] * tree_size

	for _ in range(n):
		cmd = list(map(int, input().split()))
		if cmd[0] == 1:
			ret = query(1, 1, MAX, cmd[1])
			print(ret)
			update(1, 1, MAX, ret, -1)
		else:
			update(1, 1, MAX, cmd[1], cmd[2])