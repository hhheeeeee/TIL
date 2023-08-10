# 3-2의 create_user활용
# 주어진 유저 정보 리스트와 모든 유저 등록
# 반환된 유저 정보를 하나의 리스트에 담아 출력 map함수 사용

number_of_people = 0

def increase_user():
    global number_of_people
    number_of_people += 1

def create_user(name, age, address):
    increase_user()
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address

    print(name +"님 환영합니다!")
    
    return user_info

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

result = list(map(create_user, name, age, address))

print(result)