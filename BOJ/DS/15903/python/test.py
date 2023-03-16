import sys
import heapq
input = sys.stdin.readline


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    q = []
    for i in a:
        heapq.heappush(q, i)

    for _ in range(m):
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        heapq.heappush(q, x + y)
        heapq.heappush(q, x + y)

    print(sum(q))
