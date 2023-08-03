import sys
sys.stdin = open('test.txt')
input = sys.stdin.readline

def check_num(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                board[i][j] = -1
                return board

def check_bingo():
    bingo = 0
    # row check
    for i in range(5):
        row = 0
        for j in range(5):
            if board[i][j] == -1:
                row += 1
        if row == 5 :
            bingo += 1
    #col check
    for j in range(5):
        col = 0
        for i in range(5):
            if board[i][j] == -1:
                col += 1   
        if col == 5:
            bingo += 1
    
    # diag check
    diag1, diag2 = 0, 0
    for i in range(5):
        if board[i][i] == -1:
            diag1 += 1
    if diag1 == 5:
        bingo += 1

    for i in range(5):
        if board[i][4-i] == -1:
            diag2 += 1
    if diag2 == 5:
        bingo += 1
    
    return bingo
    

board = [list(map(int, input().split())) for _ in range(5)]
answer = []
for i in range(5):
    answer.extend(list(map(int, input().split())))

# for num in answer[:13]: #어차피 13개 숫자까지는 빙고 절대 안 나오므로 그냥 체크
#     check_num(num)

for num in answer: # 그 이후는 하나씩 체크하면서 빙고 계산
    check_num(num)
    if check_bingo() == 3:
        print(num)
        break
