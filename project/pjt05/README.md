# pjt05

## 관통 프로젝트_version1

### 새로 배운 점

- crawling.html, crawling_advanced.html을 만들 때 **"저장 시 이미 저장되어 있는 키워드라면, 새로 생성하지 않고 검색 결과 개수를 변경합니다."** 라는 요구사항을 어떻게 처리해야할지 고민을 많이 했다.
  
  - 처음에 머리 속에 떠오르는 메서드가 `get`밖에 없어서 `try except` 구문을 이용하여 처리했다. 
  
  ```python
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
  ```
  
  - `find`메서드를 사용한 다음에 반환된 쿼리셋의 길이를 활용해서 처리해도 괜찮을 것 같다. 
  
  - 추가적으로 구글링해보니 `get_or_create`이라는 QuerySet API가 있었다.
    
    - 이는 모델 객체를 생성할 때 이미 있는 객체라면 가져오고 없으면 생성한다.
    
    - 아래 코드는 keyword에 해당하는 이름을 가진 객체가 있다면 가져오고 없다면 객체를 생성해준다.
    
    - created 값을 통해 객체 생성 여부를 파악할 수 있다.
    
    ```python
    obj, created = Trend.objects.get_or_create(name=keyword)
    ```
    
    - 만약 test 라는 이름을 가진 객체를 가져오고 없다면, field1과 field2의 값을 포함해 객체를 생성하고 싶다면 아래와 같이 defaults 부분을 제외하고 keyword인수로 값을 제공한다면 그 부분들은 모두 `get()`을 하기 위한 filter로서 사용이 된다.
    
    ```python
    obj, created = Trend.objects.get_created(
        name='test'
        defaults = {'field1' : 'value1', 
                    'field2' : 'value2'}
    )
    ```

- Trend 모델을 통해서 저장된 데이터베이스를 이용하여 히스토그램을 만드는 문제에서 DB를 Dataframe으로 어떻게 바꾸어야 할지 모르겠어서 구글링을 했다.
  
  - `from django_pandas.io import read_frame` 
  
  - django 안에서 pandas 를 쉽게 이용할 수 있도록 만들어진 패키지가 있었다.
  
  - 이를 이용하면 두 줄만으로 간단하게 DB를 dataframe 형식으로 바꿀 수 있었다.
  
  ```python
  qs = Trend.objects.all()
  df = read_frame(qs)
  ```

- 검색일자를 2023-10-13 과 같은 형식으로 사용하기 위해서 처음애 trends/models.py 에 Trend 모델에 다음 주석에 해당되는 부분과 같이 작성했는데 html에서 {{ trend.created_at }}  이 내가 원하는 형식으로 나오지 않는 문제가 생겼다.
  
  ```python
  class Trend(models.Model):
      name = models.TextField()
      result = models.IntegerField()
      search_period = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
  
      # def __str__(self):
      #     return self.created_at.strftime("%Y-%m-%d")
  ```
  
  - 해결방법은 html에서 filter를 사용하는 것이었다. {{ trend.created_at |date:"Y-m-d" }} 와 같이 뒤에 filter를 추가하니 html에서 정상적으로 작동하였다.
  
  ```django
  {% block content %}
  <h2>크롤링 기초 - 전체 기간 검색 결과</h2>
  {% for trend in trends %}   
      <p>검색결과 : {{ trend.name }} - {{trend.result}}개 / 
      검색일자 : {{ trend.created_at |date:"Y-m-d" }} </p>
      <hr>
  {% endfor %} 
  ```

## 느낀 점

- 저번주 프로젝트에서 배운 내용이 생각보다 많이 필요해서 놀랐다. 모든 수업을 소홀히 하지 않고 열심히 들어야겠다고 생각했다.
