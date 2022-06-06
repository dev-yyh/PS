import sys
input = sys.stdin.readline

def get_prev(s):
    if s == 'B':
        return 'J'
    elif s == 'O':
        return 'B'
    else:
        return 'O'

if __name__ == '__main__':
    N = int(input())
    arr = [0]+list(input().rstrip())
    dp = [float('inf') for _ in range(N)]

    dp[0] = 0
    for i in range(1, N):
        prev = get_prev(arr[i])
        for j in range(i):
            k = i - j
            if prev == arr[j]:
                dp[i] = min(dp[i], dp[j] + k*k)
    
    ret= dp[-1]
    if ret == float('inf'):
        print(-1)
    else:
        print(ret)