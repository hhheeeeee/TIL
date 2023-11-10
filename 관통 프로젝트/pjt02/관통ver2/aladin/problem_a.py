import requests
from pprint import pprint
import json




def author_works():
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
    result = []
    for item in items[:20]:
        result.append(item.get('title'))
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    print(author_works())

    