import sys
input = sys.stdin.readline

def get_suffix():
	sa = [ i for i in range(N)]
	g = [0] * (N + 1)
	ng = [0] * (N + 1)

	for i in range(N):
		g[i] = ord(S[i])
	g[N] = -1
	ng[sa[0]] = 0
	ng[N] = -1
	t = 1

	while t < N:
		sa.sort(key=lambda x:(g[x], g[min(x+t, N)]))

		for i in range(1, N):
			p, q = sa[i-1], sa[i]
			if g[p] != g[q] or g[min(p+t, N)] != g[min(q+t, N)]:
				ng[q] = ng[p] + 1
			else:
				ng[q] = ng[p]
		
		if ng[N-1] == N-1:
			break
		t = t*2
		g = ng[:]
	return sa

def get_lcp(sa):
	pos = [0] * N
	ret = [0] * N
	for i in range(N):
		pos[sa[i]] = i
	
	len = 0
	for i in range(N):
		if pos[i] == N-1:
			len = 0
			continue
		j = sa[pos[i] + 1]
		while i + len < N and j + len < N and S[i+len] == S[j+len]:
			len += 1
		ret[pos[i]] = len
		if len:
			len -= 1
	return ret

if __name__ == '__main__':
	S = input().rstrip()
	N = len(S)
	sa = get_suffix()
	lcp = get_lcp(sa)

	cnt = (N*(N+1))//2 - sum(lcp)
	print(cnt)

