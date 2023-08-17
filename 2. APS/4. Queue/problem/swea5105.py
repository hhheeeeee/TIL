import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline
from collections import deque


def BFS(i, j):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if maze[nx][ny] == -3:
                    return maze[x][y]
                if maze[nx][ny] == 0:
                    maze[nx][ny] = maze[x][y] + 1
                    q.append((nx, ny))
    return 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, input().strip()
                     )) for _ in range(N)]
    flag1, flag2 = 0, 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                maze[i][j] = 0
                sx, sy = i, j
                flag1 = 1
            if maze[i][j] == 3:
                maze[i][j] = -3
                ex, ey = i, j

                flag2 = 1
        if flag1 and flag2:
            break

    print(f'#{tc} {BFS(sx, sy)}')
