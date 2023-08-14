import sys
from collections import deque
sys.stdin = open('3.txt')
input = sys.stdin.readline

'''
NxN 인접행렬 트리를 받는다
0번 노드에서부터 DFS로 참색하여 level2에 도착할 때마다 경로 출력

9
0 1 1 0 0 0 0 0 0
0 0 0 1 1 1 0 0 0
0 0 0 0 0 0 1 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
'''

n = int(input())
visited = [False] * (n+1)
graph = [[0] for i in range(n)]
for i in range(n):
     line = list(map(int, input().split()))
     for idx, j in enumerate(line):
          if j:
               graph[i].append(idx)

def dfs(start, depth, expr):
     visited[start] = True
     if depth < 2:
          expr += f" {start}"
     if depth == 2:
          print(expr + f" {start}")

     for next in graph[start]:
          if not visited[next]:
               dfs(next, depth + 1, expr)

dfs(0, 0, "")

########################################
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * 3

def DFS(now, level):
     global visited
     visited[level] = str(now)
     if level == 2:
          print(' '.join(visited))
     for i in range(N):
          if arr[now][i] == 1:
               DFS(i, level + 1)

DFS(0,0)