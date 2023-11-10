import requests
from pprint import pprint


def ebook_list(title):
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
    'ttbkey': 'ttbsenghee98011405001',
    'Query': title,
    'QueryType': 'Book',
    'MaxResults' : 20,
    'start' : 1,
    'SearchTarget' : 'All',
    'output' : 'js',
    'Version' : '20131101',
    'OptResult' :'ebookList' 
    }

    response = requests.get(URL, params=params).json()
    try:
        paper_book = response.get('item')[0]
        ebookList = paper_book['subInfo']['ebookList']
        for ebook in ebookList:
            if float(ebook['priceSales']) <= float(paper_book['priceSales']) * 0.9:
                return [{'isbn' : ebook['isbn'], 'itemId' : ebook['itemId'],\
                         'link' : ebook['link'],'priceSales' : ebook['priceSales']}]
    except:
        return



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
