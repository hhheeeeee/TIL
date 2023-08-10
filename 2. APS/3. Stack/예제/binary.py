# 이진수 만들기
# N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오
# 단, 재귀호출을 이용하세요

# 입력 4
# 출력 10

# 입력 15
# 출력 1111

# 입력 9
# 출력 101

def binary(N):
    if N == 1:
        print('1', end = '')
        return
    if N == 0:
        print('0', end = '')
        return
    binary(N // 2)
    print(N % 2, end = "")

N = int(input())
binary(N)


#################################
def func(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        # n을 2로 나눈 몫을 재귀호출, 나머지를 문자열로 더한다.
        return func(n // 2) + str(n % 2)

N = int(input())
print(func(N))