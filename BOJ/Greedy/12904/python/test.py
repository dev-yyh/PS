import sys
input = sys.stdin.readline


if __name__ == '__main__':
    S = list(input().rstrip())
    T = list(input().rstrip())

    while len(S) != len(T):
        if T[-1] == 'A':
            T.pop()
        else:
            T.pop()
            T.reverse()

    if S == T:
        print(1)
    else:
        print(0)
