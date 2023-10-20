from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import matplotlib.pyplot as plt
from django_pandas.io import read_frame
from io import BytesIO
import base64
import pandas as pd



# Create your views here.

# 키워드 저장 및 keyword.html 렌더링
def keyword(request):
    # 요청의 메서드가 POST라면 (create)
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        # 유효성 검사 진행
        # 유효성 검사가 통과된 경우
        if form.is_valid():
            article = form.save()
            return redirect('trends:keyword')
    # 요청의 메서드가 POST가 아니라면 (new)
    else:
        form = KeywordForm()
    
    keywords = Keyword.objects.all()
    context = {
        'keywords' : keywords,
        'form': form,
    }
    return render(request, 'trends/keyword.html', context)

# 키워드 삭제 및 keyword.html로 리다이렉션
def keyword_detail(request, pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')




def search(keyword, search_period):
    
    if search_period == 'all':
        url = f'https://www.google.com/search?q={keyword}&tbs=qdr:y'
    else:
        url = f'https://www.google.com/search?q={keyword}'
    
    # 크롬 브라우저가 열림
    # 이 때, 동적인 내용들이 모두 채워진다!
    driver = webdriver.Chrome()
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    
    # result_stats = soup.select_one("div#result-stats")
    # return result_stats
    
    # 열린 페이지 소스를 받아옴
    result = soup.select_one('#result-stats')
    result = result.get_text()
    # result = soup.find('div', id='results-stats')
    
    num = ''
    for i in range(len(result)):
        if result[i] == '개':
            break
        if result[i].isdigit():
            num += result[i]
    return int(num)


# 크롤링 수행 및 crawling.html 렌더링
def crawling(request):
    keywords = Keyword.objects.all()

    for keyword in keywords:
        try:
            name = keyword.name
            trend = Trend.objects.get(name=name)
            result = search(keyword.name, 'all')
            trend.result = result
            trend.search_period = 'all'
            trend.save()
        except:
            name = keyword.name
            result = search(keyword.name, 'all')
            trend = Trend.objects.create(name=name, result=result, search_period='all')
            trend.save()
    
    trends= Trend.objects.all()
    context = {
        'trends' : trends
    }
    return render(request, 'trends/crawling.html', context)





# 크롤링 수행 후 수행결과 막대 그래프 생성 및 crawling_histogram.html 렌더링
def crawling_histogram(request):
    qs = Trend.objects.all()
    df = read_frame(qs)
    plt.clf()

    plt.figure(figsize=(10, 5))
    plt.bar(df[df['search_period'] == 'all']['name'], df[df['search_period'] == 'all']['result'])
    plt.xlabel('Keyword')
    plt.ylabel('Trends')
    plt.title('Technology Trend Analysis')
    plt.legend(loc='upper right')
    
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        # chart_image: 저장된 이미지의 경로
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_histogram.html', context)



# 지난 1년을 기준으로 크롤링 수행 후 수행결과 
# 막대그래프 생성 및 crawling_advanced.html렌더링
def crawling_advanced(request):
    keywords = Keyword.objects.all()

    for keyword in keywords:
        try:
            name = keyword.name
            trend = Trend.objects.get(name=name)
            result = search(keyword.name, 'year')
            trend.result = result
            trend.search_period = 'year'
            trend.save()
        except:
            name = keyword.name
            result = search(keyword.name, 'year')
            trend = Trend.objects.create(name=name, result=result, search_period='year')
            trend.save()
    
    qs = Trend.objects.all()
    df = read_frame(qs)
    plt.clf()

    plt.figure(figsize=(10, 5))
    plt.bar(df[df['search_period'] == 'year']['name'], df[df['search_period'] == 'year']['result'])
    plt.xlabel('Keyword')
    plt.ylabel('Trends')
    plt.title('Technology Trend Analysis')
    plt.legend(loc='upper right')
    
    
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        # chart_image: 저장된 이미지의 경로
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request, 'trends/crawling_advanced.html', context)