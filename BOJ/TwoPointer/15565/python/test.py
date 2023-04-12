import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = float('inf')
    start = 0
    end = 0
    cnt = 0
    if A[start] == 1:
        cnt += 1
    while end < len(A):
        if cnt == K:
            ans = min(ans, end - start + 1)
            if A[start] == 1:
                cnt -= 1
            start += 1
        else:
            end += 1
            if end < len(A) and A[end] == 1:
                cnt += 1

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)
