# Bootstrap Grid System

[Emmet Cheat Sheet](https://docs.emmet.io/cheat-sheet/)

1. Bootstrap Grid system
   
   - 1-1 개요
   
   - 1-2 기본구조

2. Grid system for responsive web
   
   - 2-1 개요
   
   - 2-2 Grid system Breakpoints

## 1. Bootstrap Grid system

### 1-1 개요

- 웹 페이지의 레이아웃을 조정하는데 사용되는 <mark>12개의 칼럼</mark>으로 구성된 시스템

- 12는 약수가 많기 때문에 짤 수 있는 레이어 경우의 수가 여러개 이다

- 목적 : 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움

<img title="" src="./imgsrc/grid 예시.png" alt="">



### 1-2 Grid system 기본구조

1. Container : Column들을 담고 있는 공간

2. Column : 실제 컨텐츠를 포함하는 부분

3. Gutter : 컬럼과 컬럼 사이의 여백 영역
   
   - x축은 padding, y축은 margin으로 여백 생성
   
   - 왜 padding으로 할까? margin으로 늘리면 행 자체 길이가 들어나므로

<img title="" src="./imgsrc/12 column grid.png" alt="">

- 1개의 row 안에 12칸의 column 영역이 구성

- 각 요소는 12칸 중 몇 개를 차지할 것인지 지정됨



## 1-3 추가

- display : inline block

- position

- flexbox

- grid system

- float



## 2. Responsive Web Design

### 2-1 개요

- 디바이스 종류 화면 크기에 상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술

- Bootstrap grid system에서는 12개의 column과 6개의 breakpoints를 사용하여 반응형 웹 디자인을 구현

### 2-2 Grid system breakpoints

- 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
  
  - 화면 <mark>너비</mark>에 따라 6개의 분기점 제공(xs, sm, md, lg, xl, xxl)

- 각 breakpoints마다 설정된 최대 너비값 "<mark>이상으로</mark>" 화면이 거치면 grid system 동작이 변경됨

<img title="" src="./imgsrc/grid breakpoint.png" alt="">

- The Grid System
  
  - CSS가 아닌 편집 디자인에서 나온 개념으로 구성 요소를 잘 배치해서 시작적으로 좋은 결과물을 만들기 위함
  
  - 기본적으로 안쪽에 있는 요소들의 오와 열을 맞추는 것에서 기인
  
  - 정보 구조와 배열을 체계적으로 작성하여 정보의 질서를 부여하는 시스템

- Grid cards
  
  - row-cols 클래스를 사용하여 행당 표시할 열(카드) 수를 손쉽게 제어할 수 있음
