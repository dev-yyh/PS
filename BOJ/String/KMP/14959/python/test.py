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

def pi2(S, l):
    table = [0] * (l)
    j = 0
    for i in range(1, l):
        while j and S[i] != S[j]:
            j = table[j-1]
        if S[i] == S[j]:
            j += 1
            table[i] = j
    return table

if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    table = pi2(nums[::-1], n)

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

