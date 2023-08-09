
#AB100CEDF1112F4G5
case = input()
i = 0
while i < len(case):
    name = ""
    while i < len(case) and case[i].isalpha():
        name += case[i]
        i += 1
    number = ""
    while i < len(case) and case[i].isdigit():
        number += case[i]
        i += 1
    print(name + '#' + str(int(number) + 17))