import sys
input = sys.stdin.readline


if __name__ == '__main__':
    A, B = map(int, input().split())
    prime = [0, 0] + [1 for _ in range(B - 1)]
    cnt = [0] * (B + 1)

    for i in range(2, B + 1):
        if not prime[i]:
            continue
        for j in range(i + i, B + 1, i):
            prime[j] = 0
            num = j

            while num % i == 0:
                num /= i
                cnt[j] += 1

    ans = 0
    for i in range(A, B + 1):
        if prime[cnt[i]]:
            ans += 1

    print(ans)
