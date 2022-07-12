import sys
from collections import deque
input = sys.stdin.readline

def MaxFlow(S, T):
  TotalFlow = 0
  while BFS(S, T):
    v = T
    while v != S:
      u = Visit[v]
      F[u][v]+=1; F[v][u]-=1
      v = u
    TotalFlow += 1
  return TotalFlow

def BFS(S, T):
  global Visit
  Visit = [-1]*X
  Q = deque(); Q.append(S)
  while Q:
    u = Q.popleft()
    for i in range(len(graph[u])):
      v = graph[u][i]
      Residue=C[u][v]-F[u][v]
      if Residue>0 and Visit[v]<0:
        Q.append(v); Visit[v]=u
        if v==T: return True

def FlowSwap(i, j):
  F[S][i] -= 1; F[i][S] += 1
  F[i][j] -= 1; F[j][i] += 1
  F[j][T] -= 1; F[T][j] += 1

  Check = False
  Visit = [-1]*X; Visit[S] = S
  Q = deque(); Q.append(S)
  while Q:
    u = Q.popleft()
    for w in graph[u]:
      Residue = C[u][w]-F[u][w]
      if Residue>0 and Visit[w]<0:
        Q.append(w); Visit[w]=u
        if w==T:
          Check = True; break
          
  if not Check:
    F[S][i] += 1; F[i][S] -= 1
    F[i][j] += 1; F[j][i] -= 1
    F[j][T] += 1; F[T][j] -= 1
  elif Check:
    v = T
    while v != S:
      u = Visit[v]
      F[u][v]+=1; F[v][u]-=1
      v = u
  return

N, M = map(int, input().split())
X = N+M+2; S = 0; T = N+M+1
C = [[0]*X for _ in range(X)]
F = [[0]*X for _ in range(X)]
graph = [[] for _ in range(X)]

L = list(map(int, input().split()))
for i in range(1, N+1):
  graph[0].append(i)
  graph[i].append(0)
  C[0][i] = L[i-1]

L = list(map(int, input().split()))
for i in range(N+1, N+M+1):
  graph[N+M+1].append(i)
  graph[i].append(N+M+1)
  C[i][N+M+1] = L[i-N-1]
Sum = sum(L)

for i in range(N, 0, -1):
  for j in range(N+M, N, -1):
    graph[i].append(j)
    graph[j].append(i)
    C[i][j] = 1

Max = MaxFlow(0, N+M+1)

for u in range(1, N+1):
  for v in range(N+1, N+M+1):
    C[u][v] = 0
    if F[u][v]: FlowSwap(u, v)

if Max != Sum: print(-1)
else:
  Ans = []
  for i in range(1, N+1):
    Ans.append([F[i][N+1+j] for j in range(M)])

  for i in Ans:
    print(''.join(map(str, i)))
