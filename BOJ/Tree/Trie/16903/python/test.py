import sys
input = sys.stdin.readline

def insert(x):
    cur = tree
    for i in x:
        i = int(i)
        if cur[i]:
            cur[i][2] += 1
        else:
            cur[i] = [False, False, 0]
        cur = cur[i]

def delete(x):
    cur = tree
    for i in x:
        i = int(i)
        if cur[i][2] > 0:
            cur[i][2] -= 1
        else:
            cur[i] = False
            break
        cur = cur[i]

def query(x):
    ans = '0b'
    cur = tree
    for i in x:
        i = int(i)
        if cur[1-i]:
            ans += '1'
            cur = cur[1-i]
        else:
            ans += '0'
            cur = cur[i]

    return int(ans, 2)

if __name__ == '__main__':
    M = int(input())
    tree = [False, False, 0]
    insert('0'.zfill(30))
    for _ in range(M):
        cmd, x = map(int, input().split())
        b = format(x,'b').zfill(30)
        if cmd == 1:
            insert(b)
        elif cmd == 2:
            delete(b)
        else:
            print(query(b))