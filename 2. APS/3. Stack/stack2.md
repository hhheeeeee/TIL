# stack

## [참고] 부분 집합의 합

- 재귀함수로 배열 복사하기

```python
def f(i, N):
    if i == N:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i + 1, N)
        return
N = 3
A = [1, 2, 3]
B = [0] * N
f(0, N)  # [1, 2, 3]
```

- 부분집합

```python
def f(i, N):
    if i == N:
        print(B)
        return
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return

N = 3
A = [1, 2, 3]
bit = [0] * N
f(0, N) 
# [1, 1, 0]
# [1, 0, 1]
# [1, 0, 0]
# [0, 1, 1]
# [0, 1, 0]
# [0, 0, 1]
# [0, 0, 0]
```

```python
def f(i, N):
    if i == N:
        print(bit, end = " ")
        for j in range(N):
            if bit[j]:
                print(A[j], end = " ")
        print()
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return
N = 3
A = [1, 2, 3]
bit = [0] * N
f(0, N)
# [1, 1, 1] 1 2 3 
# [1, 1, 0] 1 2 
# [1, 0, 1] 1 3 
# [1, 0, 0] 1 
# [0, 1, 1] 2 3 
# [0, 1, 0] 2 
# [0, 0, 1] 3 
# [0, 0, 0]
```

```python
def f(i, N):
    if i == N:
        print(bit, end=' ')
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
                print(A[j], end=" ")
        print(f" : {s}")
    else:
        bit[i] = 1
        f(i + 1, N)
        bit[i] = 0
        f(i + 1, N)
        return

N = 3
A = [1, 2, 3]
bit = [0] * N
f(0, N)

# [1, 1, 1] 1 2 3  : 6
# [1, 1, 0] 1 2  : 3
# [1, 0, 1] 1 3  : 4
# [1, 0, 0] 1  : 1
# [0, 1, 1] 2 3  : 5
# [0, 1, 0] 2  : 2
# [0, 0, 1] 3  : 3
# [0, 0, 0]  : 0
```

```python
def f(i, N, s):  # s : i-1 원소까지 부분집합의 합(포함된 원소의 합)
    if i == N:
        print(bit, end=' ')
        print(f" : {s}")
        return
    else:
        bit[i] = 1  # 부분집합에 A[i] 포함
        f(i + 1, N, s + A[i])
        bit[i] = 0  # 부분집합에 A[i] 미포함
        f(i + 1, N, s)
        return


N = 3
A = [1, 2, 3]
bit = [0] * N
f(0, N, 0)
 
# [1, 1, 1]  : 6
# [1, 1, 0]  : 3
# [1, 0, 1]  : 4
# [1, 0, 0]  : 1
# [0, 1, 1]  : 5
# [0, 1, 0]  : 2
# [0, 0, 1]  : 3
# [0, 0, 0]  : 0
```

```python
def f(i, N, s):  # s : i-1 원소까지 부분집합의 합(포함된 원소의 합), t 찾으러려는 합
    global cnt
    cnt += 1
    if i == N:
        if s == 10:
            print(bit)
    else:
        bit[i] = 1  # 부분집합에 A[i] 포함
        f(i + 1, N, s + A[i])
        bit[i] = 0  # 부분집합에 A[i] 미포함
        f(i + 1, N, s)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는 몇 개나 되는가?
N = 10
cnt = 0
A = [i for i in range(1, N+1)]
bit = [0] * N
f(0, N, 0)
print(cnt) # 2047
```

- i 원소의 포함 여부를 결정하면 i까지의 부분집합의 합 Si를 결정할 수 있음

- Si-1이 찾고자 하는 부분집합의 합보다 크면 남은 원소를 고려할 필요가 없음
  
  ```python
  def f(i, N, s, t):  # s : i-1 원소까지 부분집합의 합(포함된 원소의 합), t 찾으러려는 합
      global cnt
      cnt += 1
      if s == t: # i - 1원소까지의 합이 찾는 값인 경
          print(bit)
          return
      elif i == N:  # 남은 원소가 없는 경우, 모든 원소에 대한 고려 끝
          return
      elif s > t: # 남은 원소를 고려할 필요가 없는 경우
          return
  
      else:  # 남은 원소가 있고 s < t인 경우
          bit[i] = 1  # 부분집합에 A[i] 포함
          f(i + 1, N, s + A[i], t)
          bit[i] = 0  # 부분집합에 A[i] 미포함
          f(i + 1, N, s, t)
          return
  
  
  # 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는 몇 개나 되는가?
  N = 10
  cnt = 0
  A = [i for i in range(1, N + 1)]
  bit = [0] * N
  f(0, N, 0, 10)
  print(cnt)  # 349  
  f(0, N, 0, 55)
  print(cnt)  # 2047
  ```
* 추가 고려 사항
  
  * 일단 다 합하고 하나씩 빼면서 남은 구간의 합이 T미만인 경우 중단

# 부분집합/순열

- swea 4881 배열 최소 합

- 결과 저장할 배열  p만들기 p [   ,   ,   ]     i행 p[i]열 선택

```python
f(i, N)
    if i == N # 순열 완성
        
    else
        가능한 모든 원소에 대해
            P[i] 결정
            f(i + 1, N)
            P[i] 복구
```

```python
def f(i, N):
    if i == N:
        print(A)
    else:
        for j in range(i, N):  # 자신부터 오른쪽 끝까지
            A[i], A[j] = A[j], A[i]
            f(i + 1, N)
            A[i], A[j] = A[j], A[i]

A = [1, 2, 3]
f(0, 3)

```

# 분할 정복 알고리즘

```python
def Power(Base, Exponent):
    if Base == 0:
        return 1
    result = 1
    for i in range(Exponent):
        result *= Base
    return result
```

```python
def Power(Base, Exponent)
    if Exponent == 0 or Base == 0:
        return 1

    if Exponent % 2 == 0:
        NewBase = Power(Base, Exponent / 2)
        return NewBase * NewBase
    else:
        NewBase = Power(Base, (Exponent - 1) / 2)
        return (NewBase * NewBase) * Base

```

*  퀵 정렬

```python

```
