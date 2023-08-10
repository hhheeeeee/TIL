# 문제
# map 배열을 하드코딩 해주세요
# map에서 대각선 방향의 합이 가장 큰 값이 나오는 좌표를 출력하세요
# 대각선 방향의 합을 구하는 sum(y,x) 함수를 만들어서 사용
# sum(y,x)는 특정 좌표(y,x)에서 대각선 방향의 합을 반환하는 함수

map = [[3,3,5,3,1],[2,2,4,2,6],[4,9,2,3,4],[1,1,1,1,1],[3,3,5,9,2]]

def sum(y, x):
    dir = [(-1,-1),(1,1),(1,-1),(-1,1)]
    diag_sum = 0
    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if 0<=ny<5 and 0<=nx<5:
            diag_sum += map[ny][nx]
    return diag_sum

maxv = 0
for i in range(5):
    for j in range(5):
        if sum(i,j) > maxv:
            maxv = sum(i,j)
            mi, mj = i, j

print(mi,mj)
print(maxv)