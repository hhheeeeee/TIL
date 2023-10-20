# 01_PJT

## 관통 ver1

-  새로 배운 점

    **API(Application Programming Interface)**
```python
import requests

api_key = '5c62869ead74af64b64f186608d5b77d'

url = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'

# 응답을 json 형태로 변환
response = requests.get(url, params=params).json()

```
    Client가 Server에 request를 보내고 response를 받는다. 하지만 Clinet가 Server에 request를 보낼 때 위와 같이 파이썬으로도 보낼 수 있고 크롬으로 접속해서 request를 보낼 수도 있다. 

    다양한 방법에 따른 request를 Server가 받고 그 요청 방식에 따른 response를 하기 힘들기 때문에 그 사이에 API를 두어서 처리하기 쉽도록 한 것이다.

    고객이 레스토랑에 주문을 할 때 직원에게 주문을 하는 것과 유사하다

- 느낀점

    [금융감독원](https://finlife.fss.or.kr/finlife/api/fncCoApi/list.do?menuNo=700051) 사이트만 참고했을 때에는 "BaseList"라는 단어가 명시적으로 나와있지 않고 그냥 "baseinfo"라고만 나와있어서 처음에 헷갈렸었다.

    데이터를 직접 뜯어보면서 자세히 들여다보는 것이 중요하다고 느꼈다.