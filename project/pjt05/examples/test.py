import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re


def search(keyword):
    url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워진다!
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 열린 페이지 소스를 받아옴
    result = soup.select_one('#result-stats')
    result = result.get_text()
    result = str(result)
    print(result)
    # result = soup.find('div', id='results-stats')
    num = ''
    
    for i in range(len(result)):
        if result[i] == '개':
            break
        if result[i].isdigit():
            num += result[i]
    print(num)
        

search('파이썬')