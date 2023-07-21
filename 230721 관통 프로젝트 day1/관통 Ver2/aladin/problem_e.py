import json


def new_books(books_list):
    result = []

    for book in books_list:
        book_detail = json.load(
            open(f'data/books/{book["id"]}.json', encoding='utf-8'))
        year, month, date = book_detail['pubDate'].split('-')
        if int(year) == 2023:
            result.append(book['title'])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))
