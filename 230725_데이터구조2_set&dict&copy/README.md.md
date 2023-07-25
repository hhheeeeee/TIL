# Set 관련 메서드

* .add(x)
```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set) # {1, 2, 3, 4}

my_set.add(4)
print(my_set) # {1, 2, 3, 4}
```

* .clear()
```python
my_set = {1, 2, 3}
my_set.clear()
print(my_set) # set()
# 딕셔너리와 헷갈리지 않도록
```

* .remove(x)

세트에서 항목 x를 제거 - **없는거 제거하면 오류 발생**
```python 
my_set = {1, 2, 3}
print(my_set.remove(2)) # None
print(my_set)  # {1, 3}

my_set.remove(10)
print(my_set)  # KeyError
```

* .discard()

세트에서 항목 x를 제거 - **없는거 제거해도 오류X**
```python
my_set = {1, 2, 3}
print(my_set.discard(2)) # None
print(my_set)  # {1, 3}

my_set.discard(10)
print(my_set)  # {1, 3}
```

* .pop()

set에서 **임의**의 요소를 제거하고 **반환**

실행할 때마다 다른 요소를 얻는다는 의미에서의 "무작위"가 아니라 "임의"라는 의미에서 "무작위"

> By "arbitrary"  not "random

세트 내 각 요소는 해시 함수를 토해 해시값으로 변환되고 이 해시 값을 기반으로 해시 테이블에 저장됨

( + 딕셔너리 키도 해시함수를 통해 해시 값으로 변환하여 해시 테이블에 저장)
```python
my_set = {1, 3, 2, 10, 3, 7, 1}
print(my_set.pop())  # 1
print(my_set)  # {2, 3, 7, 10}

print(my_set.pop())  # 2
print(my_set)  # {3, 7, 10}
```

* .update(iterable)

list extend랑 비슷한 느낌
```python
my_set = {1, 2, 3}
my_set.update([4, 5, 1])
print(my_set)  # {1, 2, 3, 4, 5}

my_set = {1, 2, 3}
my_set.update("abc")
print(my_set)  # {1, 2, 3, 'c', 'a', 'b'}

my_set = {1, 2, 3}
my_set.update((4, 5, 6))
print(my_set)  # {1, 2, 3, 4, 5, 6}

my_set = {1, 2, 3}
my_set.update(("def"))
print(my_set)  # {1, 2, 3, 'e', 'f', 'd'}

my_set = {1, 2, 3}
my_set.update(["hij"])
print(my_set)  # {'hij', 1, 2, 3}
```

# dictionary
* .get(key [, default])

키 연결된 값 반환하거나 키가 없으면 None 혹은 기본 값을 반환

```python
my_dict = {'name': 'Alice', 'age': 23}

print(my_dict['name'])  # Alice
print(my_dict.get('name'))  # Alice

# print(my_dict['country'])  # KeyError
print(my_dict.get('country'))  # None
print(my_dict.get('country', '알 수 없음')) # 알 수 없음
```

* .keys() .values() .items()
```python
my_dict = {'name': 'Alice', 'age': 23}
print(my_dict.keys())  # dict_keys(['name', 'age'])
print(my_dict.values())  # dict_values(['Alice', 23])
print(my_dict.items())  # dict_items([('name', 'Alice'), ('age', 23)])

for key, value in my_dict.items():
    print(key, '+', value)
# name + Alice
# age + 23
```

* .pop(key [, default])
키를 제거하고 연결됐던 값을 반환(없으면 에러나 default 반환)
```python
my_dict = {'name': 'Alice', 'age': 23}

print(my_dict.pop('age')) # 23
print(my_dict) # {'name': 'Alice'}
print(my_dict.pop('country', "없음")) # 없음
print(my_dict.pop('country')) # KeyError
```

* .setdefault(key [, default])
.get이랑 비슷한데 **키가 없다면** default와 연결한 키를 딕셔너리에 추가하고 **default를 반환**
```python
my_dict = {'name': 'Alice', 'age': 23}

print(my_dict.setdefault('country', 'KOREA'))  # Korea
print(my_dict)  # {'name': 'Alice', 'age': 23, 'country': 'KOREA'}

print(my_dict.setdefault('name', 'Alice'))  # Alice
print(my_dict)  # {'name': 'Alice', 'age': 23, 'country': 'KOREA'}

print(my_dict.setdefault('name', 'daisy'))  # Alice
print(my_dict)  # {'name': 'Alice', 'age': 23, 'country': 'KOREA'}

print(my_dict.setdefault('name'))  # Alice
print(my_dict.setdefault('what'))  # None
```

* .update([other])
other가 제공하는 키/값 쌍으로 딕셔너리 갱신, **기존 키는 덮어씀**
```python
my_dict = {'name': 'Alice', 'age': 23}
other_dict = {'name': 'Jane', 'gender': 'female'}

my_dict.update(other_dict)
print(my_dict)  # {'name': 'Jane', 'age': 23, 'gender': 'female'}

my_dict.update(age=50)
print(my_dict)  # {'name': 'Jane', 'age': 50, 'gender': 'female'}

my_dict.update(country='korea')
# {'name': 'Jane', 'age': 50, 'gender': 'female', 'country': 'korea'}
print(my_dict)

my_dict.update(country='USA', age=100)
print(my_dict) # {'name': 'Jane', 'age': 100, 'gender': 'female', 'country': 'USA'}
```

```python
# 혈액형 인원 수 세기
# 결과 => {'A' : 2, 'B' : 3, 'O' : 4, 'AB' : 3}
blood_types = ['A', 'A', 'B', 'B', 'B', 'O', 'O', 'O', 'O', 'AB', 'AB', 'AB']

# []
new_dict = dict()
for blood in blood_types:
    if blood in new_dict:
        new_dict[blood] += 1
    else:
        new_dict[blood] = 1
print(new_dict)

# .get()
new_dict1 = dict()
for blood in blood_types:
    new_dict1[blood] = new_dict1.get(blood, 0) + 1
print(new_dict1)

# .setdefault()
new_dict2 = dict()
for blood in blood_types:
    new_dict2.setdefault(blood, 0)
    new_dict2[blood] += 1
print(new_dict2)

# Counter
from collections import Counter
result1 = Counter(blood_types)
print(result1)

# count
result = dict()
unique = set(blood_types)
for bl in unique:
    result[bl] = blood_types.count(bl)
print(result)

```

# 복사

```python
# 변경 가능한 데이터 타입의 복사
a = [1, 2, 3, 4]
b = a
b[0] = 100

print(a)  # [100, 2, 3, 4]
print(b)  # [100, 2, 3, 4]

# 변경 불가능한 데이터 타입의 복사
a = 20
b = a
b = 10

print(a)  # 20
print(b) # 10
```

1. 할당
    * 리스트 복사 예시
        할당 연산자(=)를 통한 복사는 해당객체에 대한 **객체 참조를 복사**
        ```python
        origin = [1, 2, 3]
        copy_list = origin
        print(origin, copy_list)  # [1, 2, 3] [1, 2, 3]

        copy_list[0] = 'hi'
        print(origin, copy_list)  # ['hi', 2, 3] ['hi', 2, 3]
        ```
2. 얕은 복사
   * 리스트 얕은 복사
        슬라이싱을 통해 생성된 객체는 원본 객체와 독립적으로 존재
        ```python
        origin = [1, 2, 3]
        copy_list = origin[:] 
        print(origin, copy_list)  # [1, 2, 3] [1, 2, 3]

        copy_list[0] = 100
        print(origin, copy_list)  # [1, 2, 3] [100, 2, 3]
        ```

        ```python
        copy_list = origin.copy()
        ```
    * 얕은 복사의 한계
        ```python
        a = [1, 2, [1, 2]]
        b = a.copy()
        b[2][0] = 999
        print(a, b)  # [1, 2, [999, 2]] [1, 2, [999, 2]]

        a = [1, 2, [1, 2]]
        b = a[:]
        b[2][0] = 999
        print(a, b)  # [1, 2, [999, 2]] [1, 2, [999, 2]]
        ```
3. 깊은 복사
   * 내부에 중첩된 모든 객체까지 새로운 객체 주소를 참조하도록 함
   ```python
   import copy

    a = [1, 2, [1, 2]]
    b = copy.deepcopy(a)
    b[2][0] = 999
    print(a, b)  # [1, 2, [1, 2]] [1, 2, [999, 2]]
   ```
