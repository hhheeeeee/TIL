# Many to many relationships 2

1. Many to many relationships 2
   
   - 1-1 프로필
   
   - 1-2 팔로우 기능 구현
   
   - 1-3 참고
     
     - .exists()

2. Django Fixtures
   
   - 2-1 Fixtures
   
   - 2-2 참고
     
     - 모든 모델을 한번에 dump 하기
     
     - loaddata 시 encoding codec 관련 에러 발생 경우

3. Improve query
   
   - 3-1쿼리 개선

---

# 1. 팔로우

## 1-1 프로필

- 각 회원의 개인 프로필 페이지에 팔로우 기능을 구현하기 위해 프로필 페이지를 먼저 구현

- url 작성

- view 함수 작성

- profile 템플릿 작성

- 프로필 링크로 이동할 수 있는 링크 작성

- 프로필 페이지 결과 확인  

## 1-2 팔로우 기능 구현

- User(M) - User(N)
  
  - 0명 이상의 회원은 0명 이상의 회원과 관련
  
  - 회원은 0명 이상의 팔로워를 가질 수 있고,
  
  - 0명 이상의 다른 회원들을 팔로잉 할 수 있음
  
  - 

- ManyToManyField 작성

> - 참조
>   
>   - 내가 팔로우 하는 사람들(팔로잉, followings)
> 
> - 역참조
>   
>   - 상대방 입장애서 나는 팔로워 중 한 명(팔로워, followers)
> 
> **<mark>바뀌어도 상관 없으나 관계 조회 시 생각하기 편한 방향으로 정하기</mark>**

img

- Migration 진행 후 중개 테이블 확인

- url 작성

- view 함수 작성

- 프로필 유저의 팔로잉, 팔로워 수 & 팔로우 언팔로우 버튼 작성

- 팔로우 버튼 클릭 후 팔로우 버튼 병화 및 중개 테이블 데이터 확인



## 참고

### .exists()

- QuerySet에 결과가 포함되어 있으면 True를 반환하고, 결과가 포함되어 있지 않으면 False를 반환

- 큰 QuerySet에 있는 특정 객체 검색에 유용
  
  

# 2. Fixtures

- Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음
  
  - 데이터베이스 구조에 맞추어 작성되어 있음
  
  - 

- Fixture 사용목적 : 초기 데이터 제공
  
  - 필요성
  
  > - 협업하는 유저 A, B가 있다고 생각해보기
  > 1. A가 먼저 프로젝트 작업 후 github에 push
  >    
  >    - gitignore로 인해 DB는 업로드하지 않기 때문에 A가 생성한 데이터도 업로드 X
  > 
  > 2. B가 github에서 A가 push한 프로젝트를 pull (혹은 clone)
  >    
  >    - 결과적으로 B는 DB가 없는 프로젝트를 받게 됨
  > - 이처럼 Django 프로젝트의 앱을 처음 설정할 때 동일하게 준비된 데이터로 데이터베이스를 미리 채우는 것이 필요한 순간이 있음
  > 
  > - fixtures를 사용해 초기 데이터(initial data)를 제공

- Fixtures 활용
  
  - 명렁어
    
    - `dumpdata` : 생성(데이터 추출)
    
    - `loaddata`  : 로드(데이터 입력)
  
  - `dumpdata`
    
    - 데이터의 모든 데이터를 추출
    
    - 추출한 데이터는 json 형식으로 저장
    
    ```bash
    $ python manage.py dumpdata [app_name[.ModelName] [app_name[.ModelName] ...]] > filename.json
    ```
    
    - 예시1
    
    ```bash
    $ python manage.py dumpdata --indent 4 articles.article > articles.json
    ```
    
    - 예시2
    
    ```bash
    $ python manage.py dumpdata --indent 4 accounts.user > user.json
    $ python manage.py dumpdata --indent 4 articles.conment > comments.json
    ```
  
  - `loaddata`
    
    - Fixtures 데이터를 데이터베이스로 불러오기
    
    - Fixtures 파일 기본 경로
      
      `app_name/fixtures/`
    
    - Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾아 load
    
    - 예시1
      
      - db.sqlite3 파일 삭제 후 migrate 진행
      
      ```python
      # 해당 위치로 fixtues 파일 이동
      articles/
        fixtures/
           articles.json
           users.json
           comments.json
      ```
      
      - load 후 데이터가 잘 입력되었는지 확인
      
      ```bash
      $ python manage.py loaddata articles.json users.json comments.json
      ```
    
    - loaddata 순서 주의사항
      
      - 만약 loaddata를 한번에 실행하지 않고 하나씩 실행한다면 모델 관계에 따라 load 하는 순서가 중요할 수 있음
        
        - comment는 article에 대한 key 및 user에 대한 key가 필요
        
        - article은 user에 대한 key가 필요
      
      - 즉, 현재 모델 관계에서는 user -> article ->comment 순으로 data를 넣어야 오류가 발생하지 않음
  
  ## ! Fixtures 파일을 직접 만들지 말 것
  
  - 반드시 `dumpdata`명령어를 사용하여 생성

## 참고

#### 모든 모델을 한번에 dump 하기

```bash
# 3개의 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

# 모든 모델을 하나의 json 파일로
$ python manage.py dumpdata --indent 4 > data.json
```

#### loaddata 시 encoding codec 관련 에러가 발생하는 경우

- 2가지 방법 중 택 1
1. dumpdata 시 추가 옵션 작성
   
   ```bash
   $ python -Xutf8 manage.py dumpdata [생략]
   ```

2. 메모장 활용
   
   1. 메모장으로 json 파일 열기
   
   2. "다른 이름으로 저장" 클릭
   
   3. 인코딩을 UTF8로 선택 후 저장
   
   
   

# 3. Improve query

- 쿼리 개선 

- 같은 결과를 얻기 위해 DB 측에 보내는 쿼리 개수를 점차 줄여 조회하기

- 사전 준비
  
  > 데이터
  > 
  > - 게시글 10개
