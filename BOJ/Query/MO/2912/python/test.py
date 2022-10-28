import sys
import math
from functools import cmp_to_key
input = sys.stdin.readline

def cmp(x, y):
    if x[0] // sqrt != y[0] // sqrt:
        return x[0] // sqrt - y[0] // sqrt
    else:
        return x[1] - y[1]

if __name__ == '__main__':
    N, C = map(int, input().split())
    colors = [0] + list(map(int, input().split()))

    M = int(input())
    Q = []
    for i in range(M):
        A, B = map(int, input().split())
        Q.append((A, B, i))
    sqrt = math.sqrt(N)

    Q.sort(key=cmp_to_key(cmp))

    cnt = [0] * (C+1)
    ans = [0] * (M)
    for i in range(M):
        start, end, idx = Q[i]
        if i == 0:
            for j in range(start, end+1):
                cnt[colors[j]] += 1
        else:
            prev_s, prev_e, _ = Q[i-1]
            for j in range(prev_s, start):
                cnt[colors[j]] -= 1
            for j in range(start, prev_s):
                cnt[colors[j]] += 1
            for j in range(prev_e+1, end+1):
                cnt[colors[j]] += 1
            for j in range(end+1, prev_e+1):
                cnt[colors[j]] -= 1
        key = max(cnt)
        if (end - start + 1)//2 < key:
            ans[idx] = cnt.index(key)

    for a in ans:
        if a:
            print(f'yes {a}')
        else:
            print('no')





    