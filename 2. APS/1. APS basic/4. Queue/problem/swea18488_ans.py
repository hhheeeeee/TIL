import sys

sys.stdin = open('2.txt')
from collections import deque


def bfs(graph, start, end):
    queue = deque([(start, 0)])  # (노드, 환승 횟수)
    visited = set()

    while queue:
        node, transfers = queue.popleft()
        if node == end:
            return transfers

        for next_node in graph[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, transfers + 1))

    return -1  # 도달할 수 없는 경우


# 입력 처리
m, n = map(int, input().split())
k = int(input())
bus_routes = {}  # 각 버스의 노선을 저장할 딕셔너리

for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    bus_routes[b] = [(x1, y1), (x2, y2)]

sx, sy, dx, dy = map(int, input().split())

# 그래프 생성
graph = {}
for b, route in bus_routes.items():
    for x, y in route:
        node = (x, y)
        if node not in graph:
            graph[node] = []
        graph[node].append(b)
print(graph)

# 출발지와 목적지 간의 최소 환승 횟수 계산
start = (sx, sy)
end = (dx, dy)
min_transfers = bfs(graph, start, end)

print(min_transfers)
