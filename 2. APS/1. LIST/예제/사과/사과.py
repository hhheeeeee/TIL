import sys
sys.stdin = open('aa.txt')
input = sys.stdin.readline
        # 오     밑으로  왼쪽으로  위로
#dir = [(1, 0),(-1, 0), (0,-1), (1,0)]

def which_quadrant(sx, sy, nx, ny):
    if nx - sx > 0 and ny - sy > 0:
        return 4  
    if nx - sx > 0 and ny - sy < 0:
        return 3 
    if nx - sx < 0 and ny - sy > 0:
        return 1 
    if nx -sx < 0 and ny - sy < 0:
        return 2 
    
def change_dir(quadrant, dir):
    global total_right
    
    if dir == 0:
        if quadrant == 1 or quadrant == 2:
            dir = 3
            total_right += 3
            return dir
        if quadrant == 4:
            dir = 1
            total_right += 1
            return dir
        if quadrant == 3:
            dir = 2
            total_right += 2
            return dir
    
    if dir == 1:
        if quadrant == 1 or quadrant == 4:
            dir = 0
            total_right += 3
            return dir
        if quadrant == 2:
            dir = 3
            total_right += 2
            return dir
        if quadrant == 3:
            dir = 2
            total_right += 1
            return dir
    
    if dir == 2:
        if quadrant == 3 or quadrant == 4:
            dir = 1
            total_right += 3
            return dir
        if quadrant == 2:
            dir = 3
            total_right += 1
            return dir
        if quadrant == 1:
            dir = 0
            total_right += 2
            return dir

    if dir == 3:
        if quadrant == 2 or quadrant == 3:
            dir = 2
            total_right += 3
            return dir
        if quadrant == 1:
            dir = 0
            total_right += 1
            return dir
        if quadrant == 4:
            dir = 1
            total_right += 2
            return dir


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    apple = dict()
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0:
                apple_num = graph[i][j]
                apple[apple_num] = (i, j)
    total_right = 1
    apple_num = len(apple)
    now_dir = 1
    sx, sy = apple[1][0], apple[1][1]
    for i in range(2, apple_num+1):
        ax, ay = apple[i][0], apple[i][1]
        quad = which_quadrant(sx, sy, ax, ay)
        #print(f'quad : {quad}')
        now_dir = change_dir(quad, now_dir)
        #print(f'now_dir : {now_dir}')
        sx, sy = apple[i][0], apple[i][1]
    print(f'#{tc} {total_right}')

