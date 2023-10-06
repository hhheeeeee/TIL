# 231006 PJT

## 새로 배운 점

1. Django에서 matplotlib를 import하여 그래프를 그린 후 그 그래프를 화면에 출력하기
   
   - 기존 강의에서는 static 을 이용해서 이미 저장되어 있는 이미지 파일을 출력하는 방법만 배웠는데 이번 프로젝트를 통해서  buffer를 사용하여 파일로 저장하지 않고 메모리 단에서 작업하는 방법을 배웠다.
   
   - `from io import BytesIO` 을 하여 외부에서 불러온 후, `buffer = BytesIO()`와 같은 방식으로 비어 있는 버퍼를 생성한 뒤, `plt.savefig(buffer, format='png')`로 버퍼에 그래프를 저장하고 `    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')`버퍼의 내용을 인코딩한 뒤 마지막으로 `buffer.close()` 버퍼를 닫아준다. context에 넣을 때는 `'chart_image': f'data:image/png;base64,{image_base64}',`같은 형식으러 저장된 이미이지의 경로를 이용하여 넣어준다.
   
   - view.py에서 matplotlib.pyplot을 쓸 때에는 꼭 `plt.switch_backend('Agg')`을 넣어줘야 터미널에서 오류가 나지 않는다는 사실도 알게 되었다.
   
   - ```python
     # io: 입출력 연산을 위한 Python 표준 라이브러리
     # BytesIO: 이진 데이터를 다루기 위한 버퍼를 제공
     # 버퍼: 임시 저장 공간
     # 파일 시스템과 유사하지만,
     # 실제로 파일로 만들지 않고 메모리 단에서 작업할 수 있다.
     from io import BytesIO
     
     # 텍스트 <-> 이진 데이터를 변환할 수 있는 모듈
     import base64
     
     def example(request):
         # 비어있는 버퍼를 생성
         buffer = BytesIO()
         #plt그리기
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
          return render(request, 'example.html', context)
     
     
     ```

2. html에서 dataframe을 표시하는 방법
   
   - `<table>`이라는 tag를 처음 사용해보았다.
     
     - 표를 만드는데 사용되는 태그
   
   - `<th>` : table head. 표의 제목을 쓰는 역할, 기본값은 굵은 글씨에 중앙 정렬
   
   - `<tr>` : table row. 가로줄을 만드는 역할, 기본값은 보통 글씨체에 왼쪽 정렬
   
   - `<td>` : table data,  셀을 만드는 역할, 기본값은 보통 글씨체에 왼쪽 정렬
   
   ```html
     <table>
       <tr>
         {% for column in df.columns %}
           <th>{{ column }}</th>
         {% endfor %}
       </tr>
       {% for row in df.values %}
         <tr>
           {% for value in row %}
             <td>{{ value }}</td>
           {% endfor %}
         </tr>
       {% endfor %}
     </table>
   ```

### 느낀점

- 이전에는 jupyter notebook에서만 dataframe을 다뤄봤는데 그 때는 dataframe을 조작하거나 그래프를 그리면  바로바로 결과를 눈으로 확인할 수 있기 때문에 좀 더 편했는데 장고의 views.py 안에 함수에서 그래프를 만들고 runserver를 통해 결과를 확인하다 보니 오류를 발견하기 너무 힘들었다. 
  
  - 별도로 jupyternotebook을 켜놓고 dataframe을 따로 조작하고 그 결과물만 가져다 썼다면 훨씬 빠르게 작업할 수 잇을 것 같다.

- 간단한 이미지 하나만 버퍼에 저장해놓고 출력하는데도 많은 과정이 필요하다는 것을 알게 되었다. 버퍼를 만들고 비어있는 버퍼에 이미지를 저장하고 버퍼의 내용을 인코딩하고 다시 디코딩한 다음 버퍼를 닫고 경로를 URI 형식으로 다시 만들고 하는 과정이 힘들었다.

- 가장 시간이 오래걸렸던 부분은 problem1.html에서 date열에서 자꾸 데이터가 줄바꿈되서 나오는 것을 한 줄로 나오게 하는 부분이었다. date라는 열 이름은 짧은 반면에 데이터는 '2022-10-06'과 같이 상대적으로 길어서 생기는 문제였다.
  
  - 처음에는 `{% if column == 'date' %}`이런 식으로 조건문을 사용해서 date에 해당하는 부분만 class를 만든 후에 width를 넓게 지정해주려고 했는데 표의 제목 부분은 문제가 없었으나 `{% for row in df.values %}` 이 for문 안에서 어떻게  date에 해당하는  값들만 지정하는지 알아내지 못했다. 결국 주변의 도움을 받아서 다음과 같은 style을 추가했더니 문제가 해결되었다.
  
  ```css
  th:nth-child(1) {
    padding: .5rem 2.5rem;
  }
  ```
  
  - 나중에 더 찾아보니 다음과 같은 더 간단한 방식이 있다는 것을 알게 되었다.
  
  ```css
  td {
      white-space: nowrap;
  }
  ```

- 다음으로 어려움을 겪었던 문제는 Problem2에서는 이렇게 `dt.date`로 묶었더니 잘 되어서 
  
  ```python
  Day_temperature = df.groupby(df['Date'].dt.date)[['TempHighF', 'TempAvgF', 'TempLowF']].mean()
  
  ```
  
  problem3에서도 같은 방식으로 `dt.month`로 묶었더니 2021-01과 2022-01이 같은 범주로 묶이는 문제가 발생하였다. 구글링해보니 데이터 타입이 `datetime`인 경우 `.dt.to_period('M')` 같은 방식으로 하면 월별로 잘 묶인다는 사실을 알게 되었다. 


