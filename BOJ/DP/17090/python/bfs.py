import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    for x in range(N):
        for y in range(M):
            nx = dic[arr[x][y]][0] + x
            ny = dic[arr[x][y]][1] + y
            
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                visited[x][y] = 1
                q.append((x, y))
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1

        for d in r_dic:
            nx = r_dic[d][0] + x
            ny = r_dic[d][1] + y
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 0 and arr[nx][ny] == d:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return cnt

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dic = {'U':(-1, 0), 'R':(0, 1), 'D':(1, 0), 'L':(0, -1)}
    r_dic = {'U':(1, 0), 'R':(0, -1), 'D':(-1, 0), 'L':(0, 1)}

    print(bfs())