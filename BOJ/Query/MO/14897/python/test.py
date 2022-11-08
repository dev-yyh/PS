import sys
import math
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    A = [0] + list(map(int, input().split()))
    comp = {}
    idx = 1
    for i in range(1, N+1):
        if not A[i] in comp:
            comp[A[i]] = idx
            A[i] = idx
            idx += 1
        else:
            A[i] = comp[A[i]]
    cnt = [0] * (idx+1)

    Q = int(input())
    querys = [list(map(int, input().split())) + [i] for i in range(Q)]
    sqrt = math.sqrt(N)
    querys.sort(key=lambda x:(x[0]//sqrt ,x[1]))

    ans = [0] * (Q)
    ret = 0
    for i in range(Q):
        start, end, idx = querys[i]
        if i == 0:
            for j in range(start, end+1):
                if cnt[A[j]] == 0: ret += 1
                cnt[A[j]] += 1
        else:
            prev_s, prev_e, _ = querys[i-1]
            for j in range(prev_s, start):
                cnt[A[j]] -= 1
                if cnt[A[j]] == 0: ret -= 1
            for j in range(start, prev_s):
                if cnt[A[j]] == 0: ret += 1
                cnt[A[j]] += 1
            for j in range(prev_e+1, end+1):
                if cnt[A[j]] == 0: ret += 1
                cnt[A[j]] += 1
            for j in range(end+1, prev_e+1):
                cnt[A[j]] -= 1
                if cnt[A[j]] == 0: ret -= 1
        ans[idx] = ret

    for a in ans:
        print(a)
