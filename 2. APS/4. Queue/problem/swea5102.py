import sys
sys.stdin = open('3.txt')
input = sys.stdin.readline
from collections import deque

def BFS(S, G):
    q = deque([[S, 0]])
    visited[S] = True
    while q:
        now, cnt = q.popleft()
        if now == G:
            return cnt
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                q.append([next, cnt+1])
    return 0

for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    S, G = map(int, input().split())
    print(f'#{tc} {BFS(S, G)}')

