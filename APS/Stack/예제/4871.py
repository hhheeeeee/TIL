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

