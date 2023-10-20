import requests
from pprint import pprint
import json

def author_other_works(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
    'ttbkey': 'ttbsenghee98011405001',
    'Query': title,
    'QueryType': 'Book',
    'MaxResults' : 1,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

    response = requests.get(URL, params=params).json()
    items = response.get('item')
    try:
        author = items[0]['author'].split(',')[0].strip(' (지은이)')
        isbn = items[0]['isbn']
    except:
        return 

    params1 = {
    'ttbkey': 'ttbsenghee98011405001',
    'Query': author,
    'QueryType': 'Book',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'Book',
    'output' : 'js',
    'Version' : '20131101'
}

    response1 = requests.get(URL, params=params1).json()
    items1 = response1.get('item')
    result = []
    for item in items1:
        if len(result) == 5:
            return result
        if item['isbn'] == isbn:
            continue
        result.append(item['title'])



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
