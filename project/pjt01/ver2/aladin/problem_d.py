import os
import json


def best_book(books_list):
    maxrate = 0
    subdir_names = os.listdir("data/books")
    for file_name in subdir_names:
        book = open("data/books/" + file_name, encoding='utf-8')
        book_detail = json.load(book)
        if book_detail["customerReviewRank"] > maxrate:
            maxrate = book_detail["customerReviewRank"]
            maxratebook = book_detail["title"]

    return maxratebook


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
