import sys
input = sys.stdin.readline

def pi(S, l):
    table = [0] * (l)
    i = 1
    len = 0
    while i < l:
        if S[i] == S[len]:
            len += 1
            table[i] = len
            i += 1
        else:
            if len != 0:
                len = table[len-1]
            else:
                table[i] = 0
                i += 1
    return table

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    table = pi(nums[::-1], n)

    total = float('inf')
    k = 0
    p = 0
    for i in range(n):
        kk = n - (i+1)
        pp = i+1 - table[i]
        if kk + pp < total:
            k = kk
            p = pp
            total = k + p
    print(k, p)

