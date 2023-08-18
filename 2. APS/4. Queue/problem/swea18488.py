import sys

sys.stdin = open('2.txt')
from collections import deque

def bfs(s, end):
    q = deque([(s, 0)])
    visited = [False] * (k+1)
    visited[s] = True
    while q:
        now, cnt = q.popleft()
        if now in end:
            return cnt + 1
        for next in adj[now]:
            if not visited[next]:
                visited[next] = True
                q.append((next, cnt+1))


M, N = map(int, input().split())
k = int(input())
bus = deque([])
adj = [[] for _ in range(k + 1)]
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    bus.append((b, x1, y1, x2, y2))
sx, sy, ex, ey = map(int, input().split())
start = deque([])
end = []
# 1번부터 돌면서 나랑 겹치는 구간 있는 버스는 adj에 추가
while bus:
    # now, x1, y1, x2, y2 = bb[0], bb[1], bb[2], bb[3], bb[4]
    now, x1, y1, x2, y2 = bus.pop()
    MAP = [[0] * (M+2) for _ in range(N+2)]
    row = list(range(min(x1, x2), max(x1, x2) + 1))
    col = list(range(min(y1, y2), max(y1, y2) + 1))
    for c in col:
        for r in row:
            MAP[c][r] = 1
    if sx in row and sy in col:
        start.append(now)
    if ex in row and ey in col:
        end.append(now)
    for b in bus:
        new, nx1, ny1, nx2, ny2 = b[0], b[1], b[2], b[3], b[4]
        nrow = list(range(min(nx1, nx2), max(nx1, nx2) + 1))
        ncol = list(range(min(ny1, ny2), max(ny1, ny2) + 1))
        for c in ncol:
            for r in nrow:
                if MAP[c][r] == 1:
                    if now not in adj[new]:
                        adj[new].append(now)
                    if new not in adj[now]:
                        adj[now].append(new)

# print(adj)
result = []
while start:
    s = start.pop()
    c = bfs(s, end)
    result.append(c)
print(min(result))



