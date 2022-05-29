import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve(idx):
    if idx >= L:
        return 1

    if dp[idx] != -1:
        return dp[idx]
    dp[idx] = 0
    if idx+1 < L and 10 <= int(card[idx]+card[idx+1]) <= 34:
        dp[idx] += solve(idx+2)
    
    if card[idx] != '0':
        dp[idx] += solve(idx+1)

    return dp[idx]

if __name__ == '__main__':
    card = input().rstrip()
    L = len(card)
    dp = [-1 for _ in range(L)]

    print(solve(0))