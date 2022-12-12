import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    cnt = [0] * 1000001
    for a in A:
        cnt[a] += 1

    ans = [-1] * (N)
    S = []
    for i in range(N):
        while S and cnt[A[S[-1]]] < cnt[A[i]]:
            ans[S.pop()] = A[i]
        S.append(i)
    print(' '.join(map(str, ans)))
