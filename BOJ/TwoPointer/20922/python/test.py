import sys
from collections import defaultdict
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = defaultdict(int)

    start = 0
    ans = 0
    for end in range(N):
        cnt[A[end]] += 1
        while K < cnt[A[end]]:
            cnt[A[start]] -= 1
            start += 1

        ans = max(ans, end - start + 1)

    print(ans)
