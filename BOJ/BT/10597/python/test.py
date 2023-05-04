import sys
input = sys.stdin.readline


def dfs(idx, arr):
    if idx == len(N):
        print(*arr)
        return

    num = int(N[idx])
    if idx < len(N) and num <= L and not visited[num]:
        visited[num] = 1
        arr.append(num)
        dfs(idx + 1, arr)
        arr.pop()
        visited[num] = 0

    num = int(N[idx: idx + 2])
    if idx + 1 < len(N) and num <= L and not visited[num]:
        visited[num] = 1
        arr.append(num)
        dfs(idx + 2, arr)
        arr.pop()
        visited[num] = 0
    return


if __name__ == '__main__':
    N = input().rstrip()
    L = len(N) if len(N) < 10 else (len(N) - 9) // 2 + 9
    visited = [0] * (L + 1)

    dfs(0, [])
