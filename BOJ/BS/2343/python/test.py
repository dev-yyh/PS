import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    right = sum(C)
    left = max(C)

    ans = 0
    while left <= right:
        mid = (left + right) // 2

        temp = 0
        cnt = 1
        for i in range(N):
            if temp + C[i] > mid:
                temp = 0
                cnt += 1

            temp += C[i]

        if cnt > M:
            left = mid + 1
        else:
            right = mid - 1

    print(left)
