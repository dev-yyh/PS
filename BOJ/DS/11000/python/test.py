import sys
import heapq
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    A.sort()
    q = [A[0][1]]

    cnt = 1
    for i in range(1, len(A)):
        S, T = A[i]
        if S < q[0]:
            cnt += 1
            heapq.heappush(q, T)
        else:
            heapq.heappop(q)
            heapq.heappush(q, T)

    print(cnt)
