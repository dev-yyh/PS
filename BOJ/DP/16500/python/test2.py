import sys
input = sys.stdin.readline

def dfs(idx):
	if idx == len(S):
		return 1
	
	if dp[idx]:
		return dp[idx]
	
	for b in B:
		if idx + len(b) > len(S): 
			continue
		for i in range(len(b)):
			flag = True
			if S[idx+i] != b[i]:
				flag = False
				break
		if flag:
			dp[idx] = dfs(idx+len(b))
	return dp[idx]

if __name__ == '__main__':
	S = input().rstrip()
	N = int(input())
	B = [input().rstrip() for _ in range(N)]
	dp = [0 for _ in range(len(S))]

	print(dfs(0))
