# 오토마타 전이그래프 활용
import sys
input = sys.stdin.readline

match = {
    0: (1, 2),
    1: (-1, 0),
    2: (3, -1),
    3: (4, -1),
    4: (4, 5),
    5: (1, 6),
    6: (7, 6),
    7: (4, 0)
}

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        P = input().rstrip()
        state = 0
        for p in map(int, P):
            state = match[state][p]
            if state == -1:
                break
        if state in (0, 5, 6):
            print('YES')
        else:
            print('NO')