import sys
input = sys.stdin.readline

if __name__ == '__main__':
	S = input().rstrip()
	N = int(input())
	B = [input().rstrip() for _ in range(N)]
	dp = [0 for _ in range(len(S) + 1)]
	dp[0] = 1
	for i in range(len(S)):
		if dp[i] == 0:
			continue
		for b in B:
			if S[i:].startswith(b):
				dp[i + len(b)] = 1
	
	print(dp[-1])