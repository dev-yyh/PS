import sys
input = sys.stdin.readline

MOD = 1000000007

def pow (n, m):
    if m == 0:
        return 1
    
    ret = pow(n, m//2)
    if m % 2 == 0:
        return ret * ret % MOD
    else:
        return ret * ret * n % MOD

def pow2 (n, m):
    ret = 1
    while m:
        if m & 1:
            ret = (ret * n) % MOD
        n = (n*n) % MOD
        m = m // 2
    return ret

if __name__ == '__main__':
    M = int(input())
    ans = 0
    for _ in range(M):
        N, S = map(int, input().split())
        ans += (S * pow2(N , MOD-2)) % MOD

    print(ans % MOD)