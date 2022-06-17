import sys
input = sys.stdin.readline

if __name__ == "__main__":
    A = input().rstrip()
    B = input().rstrip()
    a_len = len(A)
    b_len = len(B)
    dp = [[0 for _ in range(b_len+1)] for _ in range(a_len+1)]

    for i in range(1, a_len+1):
        dp[i][0] = i
    
    for j in range(1, b_len+1):
        dp[0][j] = j
    
    for i in range(1, a_len+1):
        for j in range(1, b_len+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    print(dp[a_len][b_len])