import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    dp = [float('inf') for _ in range(N+8)]

    dp[0] = 0
    for i in range(1, N+1):
        for coin in [1, 2, 5, 7]:
            dp[i] = min(dp[i], dp[i-coin])
        dp[i] += 1

    print(dp[N])