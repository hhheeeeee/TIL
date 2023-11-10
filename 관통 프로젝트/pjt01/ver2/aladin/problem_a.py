import json
from pprint import pprint


def book_info(book):
    result = dict()
    result['title'] = book.get('title')
    result['author'] = book.get('author')
    result['id'] = book.get('id')
    result['priceSales'] = book.get('priceSales')
    result['description'] = book.get('description')
    result['cover'] = book.get('cover')
    result['categoryId'] = book.get('categoryId')

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)
    pprint(book_info(book))
