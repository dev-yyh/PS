import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve(depth, node):
	global ret
	if depth == 0:
		ret += P[node]
		return P[node]

	left_node = solve(depth-1, node*2+1)
	right_node = solve(depth-1, node*2+2)
	ret += P[node] + abs(left_node - right_node)

	return P[node] + max(left_node, right_node)

if __name__ == "__main__":
	ret = 0
	k = int(input())
	P = [0] + list(map(int, input().split()))
	solve(k, 0)
	print(ret)
