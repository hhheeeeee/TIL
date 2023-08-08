
i, buho, result = 0, 0, 0
exp = input().strip()
while i < len(exp):
    if exp[i] == '-':
        buho = 1
        i += 1
    elif exp[i] == '+':
        buho = 0
        i += 1

    subnum = 0
    while i < len(exp) and exp[i] != '+' and exp[i] != '-':
        subnum = (subnum * 10) + int(exp[i])
        i += 1

    if buho == 1:
        result -= subnum
    else:
        result += subnum

print(result)