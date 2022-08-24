import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    min_value = float('inf')
    for i in range(N):
        l = i+1
        r = N-1
        while l < r:
            ret = arr[l] + arr[r] + arr[i]
            if min_value > abs(ret):
                min_value = abs(ret)
                ans = [arr[i], arr[l], arr[r]]
            if ret < 0:
                l = l + 1
            else:
                r = r - 1
        if min_value == 0:
            break
    print(*ans)