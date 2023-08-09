# 함수를 호출할 때마다 유저 수 1 증가하도록
# number_of_people증가하도록 

number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

increase_user()
print(number_of_people)
