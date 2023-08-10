# 1~9의 카드 중에 다섯개의 카드 입력 받는다
# 12345 => 497
# 다섯개 중에서 4개 뽑는다.
# 뽑을 때마다 전에 뽑았던 카드 번호와 간격이 3이하로 차이나는 중복순열이 몇가지인가?

# 1111 ok
# 1112 ok
# 1113 ok
# 1114 ok
# 1115 no
# 1121 ok

N = list(input().strip())

# 뽑은 카드가 유효한지 확인
def isvalid(result):
    # 1115
    for i in range(3):
        if abs(int(result[i]) - int(result[i+1])) > 3:
            return False
    return True

# 중복 순열 만들기
def comb(start):
    global cnt
    if len(result) == 4:
        if isvalid(result):
            cnt += 1
        return

    for i in range(start, len(N)):
        result.append(N[i])
        comb(0)
        result.pop()


result = []
cnt = 0
comb(0)
print(cnt)

############################################

card = list(input())
path = [0] * 4
cnt = 0

def card_cnt(level):
    global cnt
    # 4장의 카드를 뽑았으면 경우의 수 증가
    if level == 4:
        cnt += 1
        return  # 재귀호출종료
    for i in range(5):  # 5개의 카드중 하나 선택
        path[level] = card[i]  # 현재 레벨 경로에 -> 선택한 카드를 저장
        # 연속된 카드간의 차이가 4이상이면 -> 다음 카드 선택 -> 백트래킹
        if int(path[level]) - int(path[level-1]) >= 4:
            continue
        if int(path[level-1]) - int(path[level]) >= 4:
            continue
        # 다음 레벨로 재귀 호출
        card_cnt(level+1)
card_cnt(0)
print(cnt)
