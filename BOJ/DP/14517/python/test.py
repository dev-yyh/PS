import sys
input = sys.stdin.readline

MOD = 10007
if __name__ == '__main__':
    S = input().rstrip()
    length = len(S)
    dp = [[0] * length for _ in range(length)]
    for i in range(length):
        dp[i][i] = 1
    
    for L in range(1, length):
        for left in range(length):
            right = left+L
            if right >= length:
                break
            dp[left][right] = dp[left+1][right] + dp[left][right-1] - dp[left+1][right-1]
            if S[left] == S[right]:
                dp[left][right] += dp[left+1][right-1] + 1
            
            dp[left][right] = (dp[left][right] + MOD)%MOD
    
    print(dp[0][length-1])
