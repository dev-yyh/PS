import sys
input = sys.stdin.readline

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int, input().split()))
        M = int(input())
        dp = [0 for _ in range(M+1)]
        dp[0] = 1
        for c in C:
            for i in range(c, M+1):
                dp[i] += dp[i-c]

        print(dp[M])