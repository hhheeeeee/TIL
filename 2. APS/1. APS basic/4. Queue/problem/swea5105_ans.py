# 0은 길, 1은 벽
# 출발점부터 도착지점까지 갈 수 있는 길이 있는지 판단해라
# 가능하면 1 가능하지 않다면 0 출력

direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                return i, j

def bfs(y, x):
    queue = []
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        cy, cx = queue.pop(0)
        if arr[cy][cx] == '3':
            return visited[cy][cx] - 2  # 시작과 끝을 제외
        for dy, dx in direction:
            ny = cy + dy
            nx = cx + dx
            if 0 <= ny < N and 0 <= nx < N:  # 미로 범위
                if arr[ny][nx] != '1' and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    queue.append((ny, nx))
    return 0  # 경로가 없으면 0 반환


for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(16)]
    visited = [[0] * N for _ in range(N)]
    sy, sx = start()
    print(f'#{tc} {bfs(sx, sy)}')
