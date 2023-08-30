# 중괄호, 대괄호, 숫자 섞여 있음
# 왼쪽부터 오른쪽으로 숫자들로 연산을 하려고 함
#  + []
#  * { }
# 처음 시작은 0
# 숫자는 모두 양수로 되어 있음

expression = 'ABC123[10]B{3}AT[20][10]BB{2}Q'

word = list(input().strip())
result = 0
for i in range(len(word)):
    temp = ''
    index = i + 1
    if word[i] == '[':
        while word[index] != ']':
            temp += word[index]
            index += 1
        result += int(temp)
    elif word[i] == '{':
        while word[index] != '}':
            temp += word[index]
            index += 1
        result *= int(temp)
print(result)