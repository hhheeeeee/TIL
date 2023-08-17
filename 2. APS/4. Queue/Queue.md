# Queue

[1. 큐의 특성](#큐의-특성)

[2. 큐 구현](#큐-구현)

[3. 선형 큐 이용시의 문제점](#선형-큐-이용시의-문제점)

[4. 우선순위 큐(Priority Queue)](#우선순위-큐(Priority-Queue))

[5. 큐의 활용 : 버퍼(Buffer)](#큐의-활용-:-버퍼(buffer))

[6. Deque 사용법](#deque-사용법)

[7. Queue vs Deque](#queue-deque)

### 큐의 특성

* 선형자료구조, 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조

* 선입선출구조(FIFO : First In First Out)

#### 큐의 기본 연산

* 삽입 : enQueue

* 삭제 : deQueue

* 큐 생성 : createQueue()

* 큐 공백 확인 : isEmpty()

* 큐 포화상태 확인 : isFull()

* 큐의 앞쪽에서 원소를 삭제없이 반환 : Qpeek()

* 선형큐
  
  * 1차원 배열을 이용한 큐
    
    * 큐의 크기 = 배열의 크기
    
    * front : 마지막으로 삭제된 위치
    
    * reat : 저장된 마지막 원소의 인덱스
  
  * 상태 표현
    
    * 초기 상태 : front = reat = -1
    
    * 공백 상태 : front == rear
    
    * 포화 상태 : reat == n-1

#### 큐 구현

* 삽입
  
  - 마지막 원소 뒤에 새로운 원소를 삽입하기 위해
    
    - rear값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련
    
    - 그 인덱스에 해당하는 배열 원소 Q[rear]에 item을 저장

```python
def enQueue(item):
    global rear
    if isFull():
        print("Queue-Full")
    else:
        rear += 1
        Q[rear] = item
```

- 삭제 
  
  - 가장 앞에 있는 원소를 삭제하기 위해
    
    - front값을 하나 증가시켜 큐에 남아있게 될 첫번재 원소 이동
    
    - 새로운 첫번째 원소를 리턴함으로써  삭제와 동일한 기능을 함

```python
def deQueue():
    global front
    if (isEmpty()):
        print("Queue_Empty")
    else
        front += 1
        return Q[front]
```

- 공백 상태 및 포화상태 검사 
  
  - 공백상태 : front == rear
  
  - 포화상태 : reat == n-1 ( n: 배열의 크기, n-1 :배열의 마지막 인덱스)

```python
def isEmpty():
    return front == rear

def Full():
    return rear == len(Q) - 1
```

- 검색
  
  - 가장 앞에 있는 원소를 검색하여 반환하는 연산
  
  - 현재 front의 한자리 뒤(front + 1)에 있는 원소, 즉 큐의 첫번재에 있는 원소를 반환

```python
def Qpeek():
    if isEmpty():
        print("Queue_Empty")
    else:
        return Q[front + 1]
```

#### 선형 큐 이용시의 문제점

- 잘못된 포화상태 인식
  
  - 선형 큐를 이용하여 원소의 삽입과 삭제를 계쏙할 경우, 배열의 앞 부분에 더 활용할 수 있는 공간이 있음에도 불구하고, rear = n-1인 상태, 즉 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨
  
  - 해결방법1
    
    - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동시킴
    
    - 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어짐
  
  - 해결방법 2
    
    - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
    
    - 초기 공백 상태
      
      - front = rear = 0
    
    - index의 순환
      
      - front와 rear의 위치가 배열의 마지막 인덱스인 n-1를 가리킨 후, 그 다음에는 논리적 순환을 이루어 배열의 처음 인덱스인 0으로 이동해야함
      
      - 이를 위해 나머지 연산자 mod를 사용함
    
    - front 변수
      
      - 공백 상태와 포화 상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 항상 빈자리로 둠
    
    - 공백상태 및 포화상태 검사
      
      - 공백 상태 : front == reat
      
      - 포화상태 : 삽입할 rear의 다음 위치 == 현재 front
        
        - (rear + 1) % n == front
      
      ```python
      def isEmpty():
          return front == rear
      
      def isFull():
          return (rear + 1) % len(cQ) == f
      ront  
      ```
    
    - 삽입
      
      - 마지막 원소 뒤에 새로원 원소 삽입
      
      - rear값을 조정하여 새로운 원소를 삽입할 자리를 바련함 : rear <- (rear+1) mod n
      
      - 그 인덱스에 해당하는 배열원소 cQ[rear]에 item을 저장
      
      ```python
      def enQueue():
          global rear
          if isFull():
              print('Queue_Full')
          else:
              rear = (reat + 1) % len(cQ)
              cQ[rear] = item
      ```
    
    - 삭제
      
      - 가장 앞에 있는 원소를 삭제하기 위해
      
      - front값을 조정하여 삭제할 자리를 준비함
      
      - 새로운 front 원소를 리턴함으로써 삭제와 동일한 기능
      
      ```python
      def deQueue():
          global front
          if isEmpty():
              print("Queue_Empty")
          else:
              front = (front + 1) % len(cQ)
              return cQ[front]
      ```

### ### 우선순위 큐(Priority Queue)

- 우선 순위를 가진 항목들을 저장하는 큐

- FIFO 순서가 아니라 우선 순위가 높은 순서대로 먼저 나가게 된다
  
  - 시뮬레이션 시스템
  
  - 네트워크 트래픽 제어
  
  - 운영체제의 테스크 스케줄링

### 큐의 활용 : 버퍼(Buffer)

- 버퍼
  
  - 데이터를 한 곳에서 다른 한 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메머리의 영역
  
  - 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미

- 버퍼의 자료구조
  
  - 버퍼는 일반적으로 입출력 및 네트워크에 관련된 기능에서 이용된다
  
  - 순서대로 입력/출력/전달 되어야 하므로 FIFO 방식의 자료구조인 큐가 활용된다

### ### Deque 사용법

```python
from collections import deque

# 비어있는 큐 만들기
deque = deque()

# 원소가 있는 큐 만들기
deque = deque([1, 2, 3])

# 큐 최대 길이 명시하기(원소를 maxlen보다 더 많이 넣으면 maxlen이 자동 갱신됨)
deque = deque(maxlen=5)
```

| Method                  | Explanation                                |
| ----------------------- | ------------------------------------------ |
| deque.append(item)      | 오른쪽 끝에 새로운 원소를 삽입한다.                       |
| deque.appendleft(item)  | 왼쪽 끝에 새로운 원소를 삽입한다.                        |
| deque.pop()             | 오른쪽 끝의 원소를 제거 후 반환한다.                      |
| deque.popleft()         | 왼쪽 끝의 원소를 제거 후 반환한다.                       |
| deque.extend(array)     | 주어진 array 배열을 순환하며 오른쪽에 추가한다               |
| deque.extendleft(array) | 주어진 array 배열을 순환하며 왼쪽에 추가한다.               |
| deque.insert(n, item)   | n번 index에 원소를 추가한다.                        |
| deque.remove(item)      | 입력한 원소를 삭제한다. 같은 원소가 있을 경우 왼쪽부터 삭제된다.      |
| deque.rotate(n)         | n만큼 원소의 위치를 회전한다. (양수 : 시계방향, 음수 : 반시계 방향) |
| deque.clear()           | 모든 원소를 제거한다.                               |
| deque.reverse()         | 원소의 위치를 좌우 반전시킨다.                          |

### Queue Deque

- deque : 각 명령을 O(1)으로 지원

- queue : 멀티쓰레드 환경을 지원하기 때문에 더 느림

- list : O(n) 의 속도
