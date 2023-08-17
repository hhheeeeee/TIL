import sys
sys.stdin = open('../test.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1 ,T+1):
    line = list(input().strip())
    stack = []
    while line:
        while line:
            if stack and stack[-1] == line[0]:
                line.pop(0)
                stack.pop()
                break
            else:
                stack.append(line[0])
                line.pop(0)

    print(f'#{tc} {len(stack)}')

##########################
T = int(input())
for tc in range(1, T + 1):
    line = input().strip()
    stack = []

    for char in line:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    print(f'#{tc} {len(stack)}')