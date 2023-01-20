# dp 사용
import sys
input = sys.stdin.readline


if __name__ == '__main__':
    A, B = map(int, input().split())
    prime = [1 for _ in range(B + 1)]
    prime[0] = 0
    prime[1] = 0
    dp = [0] * (B + 1)

    for i in range(2, B + 1):
        if not prime[i]:
            continue
        dp[i] = 1
        for j in range(2 * i, B + 1, i):
            prime[j] = 0

    for i in range(2, B + 1):
        for j in range(2, B + 1):
            if i * j > B:
                break
            if prime[j]:
                dp[i * j] = dp[i] + 1

    ans = 0
    for i in range(A, B + 1):
        if prime[dp[i]]:
            ans += 1

    print(ans)
