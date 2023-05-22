import sys
from collections import deque
input = sys.stdin.readline


def dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def bfs(x, y):
    visited = set()
    q = deque()
    q.append((x, y))
    visited.add((x, y))

    while q:
        cx, cy = q.popleft()
        if dist(cx, cy, lock[0], lock[1]) <= 1000:
            return True

        for s in store:
            nx, ny = s
            if (nx, ny) not in visited and dist(cx, cy, nx, ny) <= 1000:
                visited.add((nx, ny))
                q.append((nx, ny))
    return False


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        home = list(map(int, input().split()))
        store = [list(map(int, input().split())) for _ in range(n)]
        lock = list(map(int, input().split()))

        if bfs(home[0], home[1]):
            print('happy')
        else:
            print('sad')
