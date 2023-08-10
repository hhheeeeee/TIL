# 1부터 N까지 정수
# 이 정수들을 활용한 합으로 N을 만들 수 있는 경우
# 1. 중복 조합은 안됨
# 2. 같은 정수는 2번까지만 사용 가능


# def comb(start):
#     global total
#     global cnt
#
#     if sum(result) > N:
#         return
#
#     if sum(result) == N:
#         a = sorted(result)
#         if a not in total:  # 중복 체크
#             total.append(a)
#         return
#
#     for i in range(start, N+1):
#         if used[i] < 2 and len(result) < N+1:
#             used[i] += 1
#             result.append(i)
#             comb(start)
#             result.pop()
#             used[i] -= 1
#
#
# N = int(input())
# used = [0] * (N+1)
# total = []
# result = []
# cnt = 0
# comb(1)
#
# print(len(total))




###############################

n = int(input())
used = [0] * (n + 1)  # 각 숫자의 사용 횟수를 저장할 리스트
cnt = 0
sum_value = 0  # 현재까지의 합

def func(last):
    global cnt, sum_value
    if sum_value == n:  # 합이 n과 같으면 카운트 증가
        cnt += 1
        return
    for i in range(last, n + 1):
        if i + sum_value > n:  # 합이 n을 초과하면 종료
            return
        if used[i] > 1:  # 숫자가 이미 두 번 사용되었으면 건너뜀
            continue
        used[i] += 1  # 숫자 사용 횟수 증가
        sum_value += i  # 합에 숫자 더함
        func(i)  # 재귀 호출
        sum_value -= i  # 합에서 숫자 뺌
        used[i] -= 1  # 숫자 사용 횟수 감소

func(1)
print(cnt)