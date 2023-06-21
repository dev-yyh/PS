import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, K = map(int, input().split())
    H = list(map(int, input().split()))

    arr = []
    for i in range(1, N):
        arr.append(H[i] - H[i-1])

    arr.sort(reverse=True)
    print(sum(arr[K-1:]))
