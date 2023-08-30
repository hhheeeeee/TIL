# N개의 정수가 주어졌을 때 x + - 를 적절하게 사용하여 101의 배수를 만들 수 있는 모든 수식을 출력하시오
# 주어진 정수들의 순서는 변하지 않는다.
# 만들의어진 수식 연산의 결과가 0이 되는 경우에는 유효하지 않은 수식으로 판단
# 만들어낼 수 있는 수식이 1개 이상이라면 우선적으로 x, +, - 순서대로 연산자를 사용하는 순으로 출력하시오.
# 정수 개수 N
# N개의 정수
# 반드시 1개 이상의 수식이 완성되는 정수들의 조합이 주어짐


def calcul(idx, result, expression):

    if idx == N-1:
        if result == 0:
            return
        elif result % 101 == 0:
            print(expression)
            return
        return

    # * 다음 숫자
    calcul(idx + 1, result * numbers[idx+1], expression + "*" + str(numbers[idx+1]))
    # + 다음 숫자
    calcul(idx + 1, result + numbers[idx + 1], expression + "+" + str(numbers[idx + 1]))
    # - 다음 숫자
    calcul(idx + 1, result - numbers[idx + 1], expression + "-" + str(numbers[idx + 1]))


N = int(input())
numbers = list(map(int, input().split()))
calcul(0, numbers[0], str(numbers[0]))
