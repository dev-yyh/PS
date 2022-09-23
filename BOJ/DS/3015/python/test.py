import sys
input = sys.stdin.readline

if __name__ == '__main__':
	N = int(input())
	A = list(int(input()) for _ in range(N))

	S = []
	ans = 0
	for a in A:
		while S and S[-1][0] < a:
			ans += S.pop()[1]

		if not S:
			S.append((a, 1))
			continue
		
		if S[-1][0] > a:
			S.append((a, 1))
			ans += 1
		elif S[-1][0] == a:
			cnt = S.pop()[1]
			ans += cnt
			if S:
				ans += 1
			S.append((a, cnt+1))
	
	print(ans)


