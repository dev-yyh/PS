import sys
input = sys.stdin.readline

class Node:
    def __init__(self, value):
        self.isZero = value
        self.count = 1
        self.left = None
        self.right = None

class Trie:
    def __init__(self):
        self.root = Node(None)
    def insert(self, binary):
        head = self.root

        for num in binary:
            isZero = (num == '0')
            child = head.left if isZero else head.right
            if child:
                child.count += 1    
            else:
                child = Node(isZero)
                if isZero:
                    head.left = child
                else:
                    head.right = child
            head = child
    def delete(self, binary):
        head = self.root

        for num in binary:
            isZero = (num == '0')
            child = head.left if isZero else head.right
            child.count -= 1
            if not child.count:
                if isZero:
                    head.left = None
                else:
                    head.right = None
            head = child
    # 상위에서부터 xor 하여 1이 나오는 것을 선택 (없다면 0)
    def query(self, binary):
        head = self.root

        result = '0b'
        for num in binary:
            isZero = (num == '0')
            if (head.right and isZero) or not head.left:
                child = head.right
            else:
                child = head.left
            
            result += '0' if child.isZero == isZero else '1'
            head = child
        
        print(int(result, 2))

if __name__ == '__main__':
    M = int(input())
    tree = Trie()
    tree.insert('0'.zfill(30))
    for _ in range(M):
        cmd, x = map(int, input().split())
        b = format(x,'b').zfill(30)
        if cmd == 1:
            tree.insert(b)
        elif cmd == 2:
            tree.delete(b)
        else:
            print(tree.query(b))