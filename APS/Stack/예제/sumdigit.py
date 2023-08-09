# N의 모든 자릿수를 합한 값을 출력하는 프로그램

def digit(n):
    if n < 10:
        return n
    else:
        # n을 2로 나눈 몫을 재귀호출, 나머지를 문자열로 더한다.
        return digit(n // 10) + n % 10

N = int(input())
print(digit(N))
#################################

