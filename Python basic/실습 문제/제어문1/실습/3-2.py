# create_user실행 => increase_user호출하여  number_of_people값 증가해야됨
# create_user는 name, age, address인자로 받아 user_info에 할당
# user_info 딕셔너리 반환
# create_user 호출 => 메시지 출력
# create_user 호출 결과를 출력 => user_info 딕셔너리

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

print("현재 가입된 유저 수 : ", number_of_people)
print(create_user('홍길동', 30, '서울'))
print("현재 가입된 유저 수 : ", number_of_people)
