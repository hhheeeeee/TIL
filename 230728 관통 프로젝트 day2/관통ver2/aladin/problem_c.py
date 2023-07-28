import requests
from pprint import pprint
import json


def bestseller_book():
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
    'ttbkey': 'ttbsenghee98011405001',
    'Query': '파울로 코엘료',
    'QueryType': 'Author',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

    response = requests.get(URL, params=params).json()
    items = response.get('item')
    sorted_items = sorted(items, key=lambda x: x['salesPoint'], reverse=True)
    result = []
    for item in items[:5]:
        result.append(item['title'])
    return result
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(bestseller_book())

