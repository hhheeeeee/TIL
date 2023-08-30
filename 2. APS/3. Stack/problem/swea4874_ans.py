import sys

sys.stdin = open('3.txt')
input = sys.stdin.readline


def op(a, b, c):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a // b


def forth(line):
    stack = []
    for c in line:
        if c in '+-/*':
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
                stack.append(op(a, b, c))
            else:
                return 'error'
        elif c.isdigit():
            stack.append(int(c))
        elif c == '.':
            # return stack[-1]
            return 'error' if len(stack) != 1 else stack[0]


T = int(input())
for tc in range(1, T + 1):
    line = list(input().split())
    res = forth(line)
    print(f'#{tc} {res}')
