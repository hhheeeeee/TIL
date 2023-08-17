import sys
sys.setrecursionlimit(10**9)
sys.stdin = open('../3.txt')
input = sys.stdin.readline

def dfs(now, visited):
    visited[now] = True

    for next in graph[now]:
        if not visited[next]:
            dfs(next, visited)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[0] for _ in range(V+1)]
    visited = [False] * (V+1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    S, E = map(int, input().split())
    dfs(S, visited)
    print(f'#{tc} 1' if visited[E] else f'#{tc} 0')

#####################################

def DFS(start, end):
    stack = []
    visited = [False] * (V + 1)
    stack.append(start)
    while stack:
        now = stack.pop()
        visited[now] = True
        for next in range(1, V+1):
            if node[now][next] and not visited[next]:
                stack.append(next)
    if visited[end]:
        return 1
    else:
        return 0

for tc in range(1, T+1):
    V, E = map(int, input().split())
    node = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        node[start][end] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {DFS(S, G)}')

