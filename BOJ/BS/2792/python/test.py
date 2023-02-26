import sys
import math
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())
    K = [int(input()) for _ in range(M)]
    left = 1
    right = max(K)

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for k in K:
            total += math.ceil(k / mid)

        if total > N:
            left = mid + 1
        else:
            right = mid - 1

    print(left)
