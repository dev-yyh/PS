import sys
input = sys.stdin.readline

class TrieNode:
   def __init__(self):
      self.isEnd = False
      self.child = {}

class Trie:
   def __init__(self):
      self._root =TrieNode()

   def add(self, word):
      node = self._root
      for c in word:
         if c in node.child:
            node = node.child[c]
         else:
            node.child[c] = TrieNode()
            node = node.child[c]
      node.isEnd = True

   def find(self, word):
      node = self._root
      for i, c in enumerate(word):
         if c not in node.child:
            break
         node = node.child[c]
         if node.isEnd:
            if word[i+1:] in name_set:
               return True
      return False

if __name__ == '__main__':
   C, N = map(int, input().split())
   color = [input().rstrip() for _ in range(C)]
   name = [input().rstrip() for _ in range(N)]
   Q = int(input())
   team = [input().rstrip() for _ in range(Q)]

   tree = Trie()
   for c in color:
      tree.add(c)

   name_set= set()
   for n in name:
      name_set.add(n)
   
   for t in team:
      if tree.find(t):
         print('Yes')
      else:
         print('No')
