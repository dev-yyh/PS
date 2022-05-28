import sys
input = sys.stdin.readline

if __name__ == '__main__':
    R, C = map(int, input().split())
    arr = [input().rstrip() for _ in range(R)]
    ld = [[0 for _ in range(C)] for _ in range(R)] #left-down
    rd = [[0 for _ in range(C)] for _ in range(R)] # right-down

    for i in range(R-1, -1, -1):
        for j in range(C):
            if arr[i][j] == '0': continue
            if i+1 < R and j-1 >= 0:
                ld[i][j] = ld[i+1][j-1] + 1
            else:
                ld[i][j] = 1
            if i+1 < R and j+1 < C:
                rd[i][j] = rd[i+1][j+1] + 1
            else:
                rd[i][j] = 1

    ans = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '0': continue
            min_value = min(ld[i][j], rd[i][j])
            if min_value < ans: continue
            for k in range(min_value, 0 , -1):
                if ld[i+k-1][j+k-1] >= k and rd[i+k-1][j-(k-1)] >= k:
                    ans = max(ans, k)
                    break
    print(ans)

