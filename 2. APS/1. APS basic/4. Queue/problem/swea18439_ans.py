# import sys
# sys.stdin = open('3.txt')
# input = sys.stdin.readline
from collections import deque

S = int(input())
visited = [0] * 6
arr = [[0,0,0,0,1,0],
         [1,0,1,0,0,1],
         [1,0,0,1,0,0],
         [1,1,0,0,0,0],
         [0,1,0,1,0,1],
         [0,0,1,1,0,0]
]

def BFS(now):
    q = deque()
    q.append(now)
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in range(6):
            if arr[now][i] == 1:
                q.append(i)

BFS(S)