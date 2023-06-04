import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N = int(input())
    K = int(input())
    S = list(map(int, input().split()))
    S.sort()

    temp = []
    for i in range(N - 1):
        temp.append(S[i + 1] - S[i])

    temp.sort()

    print(sum(temp[:N - K]))
