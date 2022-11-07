import sys
input = sys.stdin.readline

def mex(S):
    i = 0
    while i in S:
        i += 1
    return i

if __name__ == '__main__':
    N = int(input())
    dp = [0] * (N+1)
    dp[2] = 1

    for i in range(3, N+1):
        S = set()
        for j in range(i-1):
            S.add(dp[j] ^ dp[i-2-j])
        dp[i] = mex(S)

    print(1 if dp[N] else 2)