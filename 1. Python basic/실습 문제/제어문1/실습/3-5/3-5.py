# 3-3 활용, book.py에 decrease_book 함수 작성
# rental_book함수 : info 인자 하나만 할당받음
#                  info인자 : 신규 고객 이름, 나이 담은 딕셔너리
#                  신규 고객 나이 // 10 = 대여할 책의 수(decrease_book함수의 인자)
#                  info 인자에 사용될 딕셔너리는 many_user, map사용하여 새로운 딕셔너리 생성
#                       map은 lambda로 구현
#                       결과를 rental_book함수에 전달하여 호출, map사용
import book

number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    increase_user()
    user_info = dict()
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address

    print(name +"님 환영합니다!")
    
    return user_info

#info : {'name': '김시습', 'age': 20}
def rental_book(info):
    book.decrease_book(info['age'] // 10)
    print(f"{info['name']}님이 {info['age'] // 10}권의 책을 대여하셨습니다.")
    

many_user = list(map(create_user, name, age, address))

# info인자 : 신규 고객 이름, 나이 담은 딕셔너리 {'name': '김시습', 'age': 20, 'address': '서울'}
info = list(map(lambda user: {'name': user['name'], 'age': user['age']}, many_user))

#info를 rental_book함수에 전달하여 호출, map사용
list(map(rental_book, info))