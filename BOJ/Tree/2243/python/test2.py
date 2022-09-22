import sys 
import math
input = sys.stdin.readline

MAX = 1000000
tree_height = math.ceil(math.log2(MAX))
tree_size = 1 << (tree_height+1)
tree = [0] * tree_size

def update(idx, value) :
	end = (1 << tree_height) + idx - 1
	while end > 1 :
		tree[end] += value
		end //= 2

def find(target) :
	idx = 1
	length = 1 << tree_height
	while idx < length :
		if target > tree[idx*2] :
			target -= tree[idx*2]
			idx = idx*2 + 1
		else:
			idx = idx*2
	idx -= length
	update(idx + 1, -1)
	return idx + 1

if __name__ == '__main__':
	n = int(input())
	for _ in range(n):
		cmd = list(map(int, input().split()))
		if cmd[0] == 1:
			print(find(cmd[1]))
		else :
			update(cmd[1], cmd[2])