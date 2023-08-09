import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

# 내 자리 포함 상하좌우로 k화력씩 커짐
n, m = map(int, input().split())
k = int(input())
board = [list(input().strip()) for _ in range(n)]

bomb = []
for i in range(n):
    for j in range(m):
        if board[i][j] == '@':
            bomb.append((i, j))

while bomb:
    x, y = bomb.pop()
    board[x][y] = '%'
    for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        for f in range(1, k+1):
            nx, ny = x+(dx * f), y+(dy *f)
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] == '#':
                    break
                if board[nx][ny] == '_':
                    board[nx][ny] = '%'

for line in board:
    print("".join(line))