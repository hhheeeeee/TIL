# book.py
number_of_book = 100

def decrease_book(num_rental_book):
    global number_of_book
    number_of_book -= num_rental_book
    print('남은 책의 수 : ', number_of_book)