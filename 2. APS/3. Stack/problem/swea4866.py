import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline


def match(line):
    stack = []
    for i in line:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}':
            if not stack or (stack and stack.pop() != '{'):
                return 0
        elif i == ')':
            if not stack or (stack and stack.pop() != '('):
                return 0
    if stack:
        return 0
    else:
        return 1

def func(line):
    stack = []
    for i in line:
        # 여는 괄호면 스택에 추가
        if i == '{' or i == '(':
            stack.append(i)
        # 닫는 괄호가 중괄호면 짝이 맞는지 확인 후 제거
        elif stack and i == '}' and stack[-1] == "{":
            stack.pop()
        elif stack and i == ')' and stack[-1] == "(":
            stack.pop()
        # 닫는 괄호인데 짝이 맞지 않음 -> stack에 추가 -> append
        if i == '}' or i == ')':
            stack.append(i)
    if stack:
        return 0
    else:
        return 1


T = int(input())
for tc in range(1, T + 1):
    line = input()
    print(f'#{tc} {match(line)}')

p