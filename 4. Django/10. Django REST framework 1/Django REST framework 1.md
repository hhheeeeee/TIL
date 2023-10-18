# Django REST framework 1

1. REST API
   
   - 1-1 REST API
   
   - 1-2 자원의 식별
     
     - 1-2-1 URL 구조
   
   - 1-3 자원의 행위
   
   - 1-4 자원의 표현

2. DRF
   
   - 2-1 Serialization

3. DRF with Single Model

---

# 1. REST API

- API (Application Programming Interface)
  
  - 애플리케이션과 프로그래밍으로 소통하는 방법
  
  - 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

- Web API
  
  - 웹 서버 또는 웹 브라우저를 위한 API
  
  - 현대 웹 개발은 하나부터 열까지 직접 개발하기보다 여러 Open API 들을 활용하는 추세
  
  - 대표적인 Third Party Open API 목록
    
    - ex) Youtube API, Google Map API, Naver Papago API, Kakao Map API

- REST (Representational **State** Transfer)
  
  - API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
  
  - 약속! ( 규칙 X)

- RESTful API
  
  - REST 원리를 따르는 시스템을 RESTful 하다고 부름
  
  - **자원을 정의**하고 **자원에 대한 주소를 지정**하는 전반적인 방법을 서술
    
    - 각각 API 구조를 작성하는 모습이 너무 다르니 약속을 만들어서 다같이 통일해서 쓰자

## 1-1 REST API

-  : REST라는 설계 디자인 약속을 지켜 구현한 API

- REST에서 자원을 정의하고 주소를 지정하는 방법
  
  1. 자원의 식별
     
     - URI
  
  2. 자원의 행위
     
     - HTTP Methods
  
  3. 자원의 표현
     
     - JSON 데이터
     
     - 궁극적으로 표현되는 데이터 결과물

### 1-2 자원의 식별

- URI (Uniform Resource Identifier) 통합 자원 식별자
  
  - URL 보다 쫌 더 큰 개념
  
  - 인터넷에서 리소스(자원)을 식별하는 문자열
    
    - 가장 일반적인 URI 는 웹 주소로 알려진 URL

- URL (Uniform Resource Locator) 통합 자원 위치
  
  - 웹에서 주어진 리소스 주소
    
    - 네트워크 상에 리소스가 어디 있는지를 알려주기 위한 약속
  
  <img title="" src="./img/url.png" alt="">

#### 1-2-1 URL 구조

1. Schema (or Protocol)

2. Domain Name

3. Port
   
   - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
   
   - HTTP 프로토콜의 표준 포트
     
     - HTTP - 80
     
     - HTTPS - 443
   
   - 표준 포트만 생략 가능

4. Path
   
   - 웹 서버의 리소스 경로
   
   - 초기에는 실제 파일이 위한 물리적 위치를 나타냈지만, 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현
   
   - 예를 들어 /articles/create/가 실제 articles 폴더 안에  create 폴더 안을 아타내는 것을 아님

5. Parameters
   
   - 웹 서버에 제공하는 추가적인 데이터
   
   - '&' 기호로 구분되는 key-value 쌍 목록
   
   - 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음
     
     - 우리 수업에서 GET 으로 검색할 때 배움!

6. Anchor
   
   - 일종의 '북마크'를 나타내며 브라우저에 해당 지점에 있는 콘텐츠를 표시
   
   - fragment identifier(부분 식별자)라고 부르는 '#' 이후 부분은 서버에 전송되지 않음
   
   - https://docs.djangoproject.com/en/4.2/intro/install/#quick-install-guide 요청에서 #quick-install-guide 는 서버에 전달되지 않고 브라우저에게 해당 지점으로 이동할 수 있도록 함

### 1-3 자원의 행위

- HTTP Request Methods
  
  - 리소스에 대한 행위(수행하고자 하는 동작)를 정의
  
  - HTTP verbs 라고도 함

- 대표 HTTP Request Methods
  
  1. GET
     
     - 서버에 리소스의 표현을 요청
     
     - GET을 사용하는 요청은 데이터만 검색해야 함
     
     - read
  
  2. POST
     
     - 데이터를 지정된 리소스에 제출
     
     - 서버의 상태를 변경 
     
     - create
  
  3. PUT
     
     - 요청한 주소의 리소스를 수정
     
     - update
  
  4. DELETE
     
     - 지정된 리소스를 삭제
     
     - delete

- HTTP response status codes
  
  - 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
  
  - 5개의 응답 그룹
  1. Informational responses (100 - 199)
  
  2. Successful responses (200 - 299)
  
  3. Redirection messages (300 -399)
  
  4. Client error responses (400 -499)
  
  5. Server error responses (500 -599)

### 1-4 자원의 표현

- 그동안 서버가 응답(자원을 표현)했던 것
  
  - 지금까지 Django 서버는 사용자에게 페이지(html)만 응답하고 있었음
  
  - 하지만 서버가 응답할 수 있는 것은 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음
  
  - REST API는 이 중에서도 <mark> **JSON** </mark>타입으로 응답하는 것을 권장

- 응답 데이터 타입의 변화
  
  - 페이지(html)만을 응답하는 서버
  
  - 이제 JSON 데이터를 응답하는 REST API 서버로의 변환
  
  - DJango는 더 이상 Template 부분에 대한 역할을 담당하지 않게 되며, Front-end와 Back-end가 분리되어 구성 됨
  
  - 이제부터 Django를 사용해 RESTful API 서버를 구축할 것

### 1-5 실습

- 사전준비
  
  - 99-json-response-practice 기반 시작
  
  - 가상 환경 생성, 활성화 및 패키지 설치
  
  - migrate
  
  - 준비된 fixtures 파일을 load하여 실습용 초기 데이터 입력
  
  ```bash
  $ python manage.py loaddata articles.json
  ```
  
  - http://127.0.0.1:8000/api/v1/articles/ 요청테스트



$ python python-request-sample.py
<class 'list'>

왜? json이 하나의 큰 list에 담겨잇음!



# 2. DRF

- Django REST framework
  
  - Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

## 2-1 Serialization

- 직렬화

- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
  
  - 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정

# 3. DRF with Single Model

- postman 다운 받기 
  
  - api 개발할 때 쓰는 프로그램

- GET - List

### 3-1 GET

- 'api_view' decorator
  
  - DRF view 함수에서는 필수로 작성되며 view 함수를 식행하기 전 HTTP 메서드를 확인
  
  - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 MEthod Not Allowed로 응답
  
  - DRF view


