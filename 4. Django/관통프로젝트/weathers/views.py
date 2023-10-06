from django.shortcuts import render
import matplotlib.pyplot as plt
# io: 입출력 연산을 위한 Python 표준 라이브러리
# BytesIO: 이진 데이터를 다루기 위한 버퍼를 제공
# 버퍼: 임시 저장 공간
# 파일 시스템과 유사하지만,
# 실제로 파일로 만들지 않고 메모리 단에서 작업할 수 있다.
from io import BytesIO

# 텍스트 <-> 이진 데이터를 변환할 수 있는 모듈
import base64

import pandas as pd
csv_path = 'weathers/data/austin_weather.csv'

plt.switch_backend('Agg')

# Create your views here.
def problem1(request):
    df = pd.read_csv(csv_path)
    context = {
        'df': df,
    }
    return render(request, 'weathers/problem1.html', context)

def problem2(request):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])
    # 다른 View 함수에서 plt 를 이미 그린 상태에서
    # 다시 그리는 경우를 대비하여, 초기화를 진행
    plt.clf()

    # 날짜별 최고/평균/최저 온도 계산
    Day_temperature = df.groupby(df['Date'].dt.date)[['TempHighF', 'TempAvgF', 'TempLowF']].mean()

    plt.figure(figsize=(10, 5))

    plt.plot(Day_temperature.index, Day_temperature['TempHighF'], label='High Temperature')
    plt.plot(Day_temperature.index, Day_temperature['TempAvgF'], label='Average Temperature')
    plt.plot(Day_temperature.index, Day_temperature['TempLowF'], label='Low Temperature')

    plt.grid(visible=True)
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.title('Temperature Variation')
    plt.legend(loc='lower center')

    # 비어있는 버퍼를 생성
    buffer = BytesIO()

    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹 페이지에 표시하기 위해
    # URI 형식(주소 형식)으로 만들어진 문자열을 생성
    context = {
        # chart_image: 저장된 이미지의 경로
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem2.html', context)

def problem3(request):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'])

    # 월별 최고/평균/최저 온도의 평균 계산
    Month_temperature = df.groupby(df['Date'].dt.to_period('M'))[['TempHighF', 'TempAvgF', 'TempLowF']].mean()

    
    plt.clf()
    # 선 그래프 그리기
    plt.figure(figsize=(10, 5))
    plt.plot(Month_temperature.index.astype(str), Month_temperature['TempHighF'], label='High Temperature')
    plt.plot(Month_temperature.index.astype(str), Month_temperature['TempAvgF'], label='Average Temperature')
    plt.plot(Month_temperature.index.astype(str), Month_temperature['TempLowF'], label='Low Temperature')


    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(8))
    # 축과 라벨 설정
    plt.grid(visible=True)
    plt.xlabel('Date')
    plt.ylabel('Temperature (Fahrenheit)')
    plt.title('Temperature Variation')
    plt.legend(loc='lower right')

    # 비어있는 버퍼를 생성
    buffer = BytesIO()

    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹 페이지에 표시하기 위해
    # URI 형식(주소 형식)으로 만들어진 문자열을 생성
    context = {
        # chart_image: 저장된 이미지의 경로
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem3.html', context)


def problem4(request):
    df = pd.read_csv(csv_path)
    df = df.replace({'Events' : ' '}, 'No Events') 
    
    # "Event" 열의 값을 분리하여 새로운 열에 저장
    df['Event_Separated'] = df['Events'].str.split(' , ')

    # 분리된 값들을 개별적으로 카운트
    event_counts = df['Event_Separated'].explode().value_counts()
    plt.clf()
    # 선 그래프 그리기
    plt.bar(event_counts.index, event_counts.values)

    # 축과 라벨 설정
    plt.grid(visible=True)
    plt.xlabel('Events')
    plt.ylabel('Count')
    plt.title('Event Counts')

    # 비어있는 버퍼를 생성
    buffer = BytesIO()

    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')

    # 버퍼의 내용을 base64 로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    
    # 버퍼를 닫아줌
    buffer.close()

    # 이미지를 웹 페이지에 표시하기 위해
    # URI 형식(주소 형식)으로 만들어진 문자열을 생성
    context = {
        # chart_image: 저장된 이미지의 경로
        'chart_image': f'data:image/png;base64,{image_base64}',
    }

    return render(request, 'weathers/problem4.html', context)