import sys
input = sys.stdin.readline

if __name__ == '__main__':
    card = input().rstrip()
    L = len(card)
    dp = [[0 for _ in range(2)] for _ in range(L)]

    dp[0][0] = 1
    for i in range(1, L):
        if 10 <= int(card[i-1] + card[i]) <= 34:
            dp[i][1] = dp[i-1][0]
        
        if card[i] == '0':
            continue
        dp[i][0] = dp[i-1][0] + dp[i-1][1]

    print(sum(dp[L-1]))


