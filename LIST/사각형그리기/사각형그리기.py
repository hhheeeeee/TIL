import sys
sys.stdin = open('a.txt')
input = sys.stdin.readline



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    maxv, tcnt = 1, 0
    for sc in range(N):
        for sr in range(N):
            for i in range(sc, N):
                for j in range(sr, N):
                    if board[i][j] == board[sc][sr]:
                        square = (i-sc+1) *(j-sr+1)
                        maxv = max(maxv, square)
    
    for sc in range(N):
        for sr in range(N):
            for i in range(sc, N):
                for j in range(sr, N):
                    if board[i][j] == board[sc][sr]:
                        square = (i-sc+1) *(j-sr+1)
                        if square == maxv:            
                            tcnt += 1      

    print(f'#{tc} {tcnt}')