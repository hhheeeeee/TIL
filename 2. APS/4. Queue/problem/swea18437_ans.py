# import sys
# sys.stdin = open('3.txt')
# input = sys.stdin.readline
from collections import deque

def BFS(now):
    q = deque([now])
    q.append(now)
    while q:
        now = q.popleft()
        print(now)
        for i in range(6):
            if used[i] == 1:
                continue
            if graph[now][i] == 1:
                used[i] = 1
                q.append(i)

S = int(input())
used = [0] * 6
graph = [[0,1,0,0,1,0],
         [0,0,1,0,0,1],
         [0,0,0,1,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0],
         [0,0,0,0,0,0]
]
used[S] = 1
BFS(S)