import json
from pprint import pprint


def book_info(book, categories):
    result = dict()
    result['title'] = book.get('title')
    result['author'] = book.get('author')
    result['id'] = book.get('id')
    result['priceSales'] = book.get('priceSales')
    result['description'] = book.get('description')
    result['cover'] = book.get('cover')
    result['categoryName'] = []
    for category in categories:
        if category['id'] in book.get('categoryId'):
            result['categoryName'].append(category['name'])

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
