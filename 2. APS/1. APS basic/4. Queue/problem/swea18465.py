import sys

sys.stdin = open('1.txt')
from collections import deque
def bfs():
    q = deque([(1, 0)])
    visited[1] = True
    while q:
        now, cnt = q.popleft()
        for next in adj[now]:
            if next == N:
                return cnt + 1
            if not visited[next]:
                visited[next] = True
                q.append((next, cnt+1))
    return -1

N, M = map(int, input().split()) # 지역의 수 N과 대중교통으로이동 가능한 관계의 수 M
adj = [[] for _ in range(N+1)]
visited = [False]  * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
T = int(input())
visited[T] = True
print(bfs())