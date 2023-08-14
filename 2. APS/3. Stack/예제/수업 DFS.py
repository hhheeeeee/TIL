import sys
from collections import deque
sys.stdin = open('3.txt')
input = sys.stdin.readline

'''
DFS
n과 인접행렬을 입력받는다
항상 0번부터 탐색을 시작
자식 노트가 여러개라면 노드 번호가 작은 것부터 탐색
1 <= n < 100
노드는 0~n-1까지 있음

입력
5
0 1 1 0 0
0 0 0 1 1
0 0 0 0 0
0 0 0 0 0
'''

n = int(input())
visited = [False] * (n+1)
graph = [[0] for i in range(n)]
for i in range(n):
     line = list(map(int, input().split()))
     for idx, j in enumerate(line):
          if j:
               graph[i].append(idx)

def dfs(start, visited):

     visited[start] = True
     print(start, end = " ")
     for next in graph[start]:
          if not visited[next]:
               dfs(next, visited)

dfs(0, visited)