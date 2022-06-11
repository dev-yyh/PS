import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]
    
    dp[x][y] = 0
    xx = dic[arr[x][y]][0] + x
    yy = dic[arr[x][y]][1] + y
    dp[x][y] = dfs(xx, yy)
    
    return dp[x][y]

if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(N)]
    dp = [[-1 for _ in range(M)] for _ in range(N)]
    dic = {'U':(-1, 0), 'R':(0, 1), 'D':(1, 0), 'L':(0, -1)}

    cnt = 0
    for i in range(N):
        for j in range(M):
            cnt += dfs(i, j)
    
    print(cnt)
