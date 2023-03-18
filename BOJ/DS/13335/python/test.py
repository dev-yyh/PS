import sys
input = sys.stdin.readline


if __name__ == '__main__':
    n, w, L = map(int, input().split())
    a = list(map(int, input().split()))

    b = [0] * w
    time = 0
    weight = 0
    while b:
        time += 1
        weight -= b.pop(0)

        if a:
            if weight + a[0] > L:
                b.append(0)
            else:
                weight += a[0]
                b.append(a.pop(0))

    print(time)
