# decrease_book 함수 : 한번에 대여하는 책의 수를 정수로 받음
# 넘겨 받은 값만큼 number_of_book수 감소, 현재 남은 책 수 출력
# rental_book 함수 : 대여자 이름, 대여하는 책의 수
# rental_book 실행 => book.py호출 -> decrease_book호출 

import book

def rental_book(name, num_rental_book):
    book.decrease_book(num_rental_book)
    print(f"{name}님이 {num_rental_book}권의 책을 대여하였습니다.")


rental_book('홍길동',3)