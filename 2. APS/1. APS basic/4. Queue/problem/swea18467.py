import sys

sys.stdin = open('1.txt')


from collections import deque

def bfs(S, D):
    q = deque([S])
    while q:
        now = q.popleft()
        if now == D:
            return visited[now]
        for next in (now // 2, now * 2, now + 1, now - 1):
            if 0 <= next <= 100000 and not visited[next] and next != S:
                visited[next] = visited[now] + 1
                q.append(next)

S = int(input())
D = int(input())
visited = [0] * 100001
print(bfs(S, D))