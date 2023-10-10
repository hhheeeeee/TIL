# DB 기초 개념 정리

## 

## DB(Database)란?

- 조직화된 데이터의 모음
  
  - 우리가 프로그램에서 사용할 데이터를 구조화해서 저장만 해놓은 것
  
  - 예시) 서울 4반 학생 -> 학생1(이름, 성별, 나이,,,), 학생2(이름, 성별, 나이,,)
  
  - 저장, 조회, 삭제, 수정 등의 추가 적업은 어떻게 하는가?
    
    - 일반적으로 DBMS(Database Management System)을 DB라 부름
      
      - 즉 관리 시스템을 DB라 칭한다.

## DB의 구성요소

- 목표 : 일상 생활의 객체를 DB에 표현하고 저장

- 개체(Entity), 스키마(Schema), 테이블(Table)
  
  - 개체(Entity)
    - 저장하고자 하는 실제 객체나 개념을 정리한 것
    - 각 엔티티는 여러 속성(Attributes)으로 구성된다
    - 예시) 서울 4반 학생들의 성별, 나이에 따른 롤 티어를 분석하고 싶다.
      - 내가 무엇을 저장해야할까 ?
      - 서울 4반 학생: 이름, 성별, 나이, 롤 티어 등등
    - 관계도 : ERD(Entity Relationship Diagram)
  - 스키마(Schema)
    - 엔티티와 속성들의 구조, 관계, 제약 조건 등을 정의 한 것
    - 엔티티들을 어떻게 구조화할 지(저장할 지) 논리적으로 설계한 것
    - 예시) 서울 4반 학생
      - 이름: 문자열로 저장
      - 나이: 숫자로 저장
      - 롤티어: 문자열로 저장
  - 테이블(Table)
    - 실제로 DB에 저장되는 객체
    - 구성 요소
      - 행(Row), 레코드(Record), 튜플(Tuple)
    - 가로 줄
      - 하나의 데이터 항목
      - 열(Column), 속성(Attribute), 필드(Field)
    - 세로 줄
      - 어떤 데이터를 저장할 것인지 나타냄

- 속성(Attribute)
  
  - 엔티티가 가지는 항목으로, 저장하고 싶은 개체의 특정 항목을 의미함

- 관계(Relationship)
  
  - 두 가지 이상의 엔티티 사이의 관계
  - 예시) 추가적으로 서울 4반의 강사 정보를 관리하고 싶다.
  - 강사 정보를 따로 저장해야 한다.
  - 다 같이 저장하면, 중복이 매우 많이 발생한다!
  - "서울 4반 학생" - "강사"는 연관된 데이터. 관계가 있다라고 말한다.

# 실습

### window 에 sqlite 설치하기 문서

- [window10 에 sqlite3 설치하기 · GitHub](https://gist.github.com/yts0275/33692ef95e622b7d5cfd02cd77a4b7e6)

#### SQLITE extension 버그

- vscode 에서 `Open database` 클릭 시 버그

- vscode -> extension -> sqlite 검색

- 우측의 설정버튼 -> extension settings 클릭

- 아래의 `Sqlite: Sqlite3` 부분 지우기

---

1. superhero.sqlite3 파일 만들기

2. superheros.sql 파일 만들기

3. csv파일 같은 폴더 내로 옮겨놓기

4. 실행

```sql
CREATE TABLE superheroes (
    id INTEGER PRIMARY KEY,
    이름 TEXT NOT NULL,
    직업 TEXT NOT NULL,
    능력 TEXT,
    국적 TEXT,
    소속회사 TEXT,
    나이 INTEGER
);


-- 테이블 명 변경하기
ALTER TABLE superheroes
RENAME TO superhero;

--새로운 컬럼 추가
ALTER TABLE superhero
ADD COLUMN 가입날짜 DATE;
```

5. 터미널에서 실행

```bash
$ sqlite3 superhero.sqlite3sqlite> .mode csv
sqlite> .import superheroes.csv superhero
```

- csv 데이터가 sqlite로 쭉 들어간다

```sql






```
