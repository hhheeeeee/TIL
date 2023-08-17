# 가능한 날짜가 몇 개 있는지
# 10, 11, 12 열은 두 자릿수로 표현하고, 1 ~ 9열은 한 자리수로 표현한다.
# 즉, 7월을 07로 표현하지 않는다.
# 년도는 4자리로 표현한다.
# 날짜는 모든 달이 1 - 31일로 가정한다.
# 1- 9 일은 한자리 수로 표현한다. 즉, 3일을 03일로 표현하지 않는다.
# 년도 부분이 찢어질 수도 있지만 년도가 찢어지는 것은 무시한다.
# ex. XXXX.12.23 인 경우 년도를 무시하기에 가능한 날짜의 수는 1개이다.
# X의 개수는 최대 8개 까지 될 수 있다. XXXX.XX.XX

# [입력 가능 예시]
# 202X.1X.XX
# 2XXX.XX.X
# 2001.X.XX
# 2023.8.3X
# 2025.X.1X == 9 * 10  = 90

# 년도, 월 일 함수로 각자 만들기

def calcul_month(month):
    possible = 0
    #1 - 12
    if len(month) == 1:
        if month == 'X':  # X
            possible = 9
        else: # 1
            possible = 1
    if len(month) == 2:
        if month == 'XX': # XX
            possible = 3
        elif month[0] == 'X': # X숫자 : 10 11 12
            possible = 1
        elif month[0] == '1': # 1X : 10 11 12
            possible = 3
        elif month[0] != 'X' and month[1] != 'X': # 숫자숫자 12:
            possible = 1
    return possible

def calcul_day(day):
    possible = 0
    #1 - 31
    if len(day) == 1:
        if day == 'X':  # X
            possible = 9
        else: # 1
            possible = 1

    if len(day) == 2:
        if day == 'XX': # XX 10 - 31
            possible = 22
        elif day[0] == 'X':
            if day[1] == '1' or day[1] == '0': # X1 : 11, 21, 31 || X0 : 10, 20, 30 ==> 3개
                possible = 3
            else:
                possible = 2  # X2 : 12 22 (32x) || 13 23 (33x) ==> 2개
        elif day[0] == '1' or day[0] == '2':
            if day[1] == 'X': # 1X : 10 11 .. 19
                possible = 10
            else: # 숫자 숫자
                possible = 1
        elif day[0] == '3':
            if day[1] == 'X' : #3X : 30, 31 = > 2개
                possible = 2
            else:
                possible = 1 # 숫자숫자

    return possible

date = input().split('.')
year = date[0]
month = date[1]
day = date[2]
p_month = calcul_month(month)
p_day = calcul_day(day)
result = 1 * calcul_month(month) * calcul_day(day)
print(result)