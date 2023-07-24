# 데이터 구조

## 문자열 메서드
```python
s = "abcde"
print(s.find('a')) # 0
print(s.find('z')) # -1
```
첫번째 위치 반환. 없으면 -1

* s.replace(old, new[ , count])
```python
s = "*-*-*-*-*-*-"
new1 = s.replace("*-", 'o') # oooooo
new2 = s.replace("*-", 'o', 2) # oo*-*-*-*-
print(new1)
print(new2)
```

* s.strip([chars])
```python
s = "  *-*-*-*-*-*-   "
new1 = s.strip()
print(new1) # *-*-*-*-*-*-

s1 = "qqqqappleqqqq"
new2 = s1.strip('q')
print(new2) # apple
```

* s.split(sep = None, maxsplit = -1)
```python
# 문자열

s = "a b c d e"
new1 = s.split()
print(new1)  # ['a', 'b', 'c', 'd', 'e']

s1 = "a b c d e"
new2 = s1.split(sep=" ", maxsplit=2)
print(new2)  # ['a', 'b', 'c d e']

s2 = "a b c d e"
new3 = s2.split(maxsplit=2)
print(new3)  # ['a', 'b', 'c d e']

s4 = "a b c d e"
new4 = s4.split(2)
print(new4)  # TypeError: must be str or None, not int

a = ('abced')
print(a.split())  # ['abced']

b = ('a b c d e')
print(b.split()) # ['a', 'b', 'c', 'd', 'e']

c = {'a b c d e'}
print(c.split())  # AttributeError: 'set' object has no attribute 'split'

```
* 'seperator'.jon([iterable])
```python
s = ['a', 'b', 'c', 'd']
print("*".join(s))  # a*b*c*d

s1 = ('a', 'p', 'p', 'l', 'e')
print("-".join(s1))  # a-p-p-l-e

s1 = "apple"
print("+".join(s1))  # a+p+p+l+e

s3 = [1, 2, 3, 4]
print("*".join(s3))  # TypeError
```

## 리스트 메서드
* .append(x)

리스트 마지막에 항목 x를 추가
```python
a_list = [1, 2, 3]
a_list.append(4)
print(a_list)  # [1, 2, 3, 4]

a_list = [1, 2, 3]
a_list.append([4, 5])  
print(a_list) # [1, 2, 3, [4, 5]]

a_list = [1, 2, 3]
a_list.append((4, 5)) 
print(a_list) # [1, 2, 3, (4, 5)]

a_list = [1, 2, 3]
a_list.append("a")
print(a_list) # [1, 2, 3, 'a']
```

* .extend([iterable])

리스트에 다른 반복 가능한 객체의 모든 항목을 추가
```python
a_list = [1, 2, 3]
a_list.extend([4, 5, 6])
print(a_list)  # [1, 2, 3, 4, 5, 6]

a_list = [1, 2, 3]
a_list.extend((4, 5, 6))
print(a_list)  # [1, 2, 3, 4, 5, 6]

a_list = [1, 2, 3]
a_list.extend("456")
print(a_list)  # [1, 2, 3, '4', '5', '6']

a_list = [1, 2, 3]
a_list.extend("4 5 6")
print(a_list)  # [1, 2, 3, '4', ' ', '5', ' ', '6']

a_list = [1, 2, 3]
a_list.extend({4, 5, 6})
print(a_list)  # [1, 2, 3, 4, 5, 6]

a_list = [1, 2, 3]
a_list.extend([123])
print(a_list)  # [1, 2, 3, 123]

a_list = [1, 2, 3]
a_list.extend(123)
print(a_list)  # TypeError: 'int' object is not iterable
```
* .insert(i, x)

리스트의 지정한 인덱서 i 위치에 항목 x를 삽입
```python
a_list = [1, 2, 3]
a_list.insert(0, 'a')
print(a_list)  # ['a', 1, 2, 3]

a_list = [1, 2, 3]
a_list.insert(0, 'a b c')
print(a_list)  # ['a b c', 1, 2, 3]

a_list = [1, 2, 3]
a_list.insert(0, [4, 5])  # [[4, 5], 1, 2, 3]
print(a_list)

a_list = [1, 2, 3]
a_list.insert(0, (4, 5))
print(a_list)  # [(4, 5), 1, 2, 3]

a_list = [1, 2, 3]
a_list.insert(0, {4, 5})
print(a_list)  # [{4, 5}, 1, 2, 3]
```
* .remove(x)
  
  리스트에서 첫번재로 일치하는 항목 삭제
```python
a_list = [1, 2, 3, 2, 2, 2]
a_list.remove(2)
print(a_list)  # [1, 3, 2, 2, 2]

a_list = [1, 2, 3, 2, 2, 2]
for i in a_list:
    if i == 2:
        a_list.remove(i)
print(a_list)  # [1, 3, 2]

a_list = [1, 2, 3, 2, 2, 2]
for _ in a_list:
    a_list.remove(2)
print(a_list)  # [1, 3, 2]
```

* .pop(i)

리스트에서 지정한 인덱스의 항목을 제거하고 **반환** 

작성하지 않을 경우 마지막 항목을 제거
```python
a_list = [1, 2, 3, 4, 5]
b = a_list.pop(2)
print(a_list)  # [1, 2, 4, 5]
print(b)  # 3

a_list = [1, 2, 3, 4, 5]
b = a_list.pop()
print(a_list)  # [1, 2, 3, 4]
print(b)  # 5
```
* .clear()
  
리스트의 모든 항목 삭제
```python
a_list = [1, 2, 3, 4, 4, 5]
a_list.clear()
print(a_list) # []
```

* L.index(x, start, end)

리스트에서 첫번째로 일치하는 항목의 인덱스를 반환
```python
a_list = [1, 2, 3, 4, 5]
index = a_list.index(2)
print(index)  # 1

a_list = [1, 3, 3, 3, 2, 4, 5]
index = a_list.index(2, 3, 5)
print(index)  # 4

a_list = [1, 3, 3, 3, 2, 4, 5]
index = a_list.index(2, 3)
print(index)  # 4

a_list = [1, 3, 3, 3, 2, 4, 5]
index = a_list.index(2, ,5)
print(index)  # SyntaxError: invalid syntax

a_list = [1, 3, 3, 3, 3, 2, 5]
index = a_list.index(2, 3, 5)
print(index)  # ValueError: 2 is not in list

a_list = [1, 2, 3, 4, 5]
index = a_list.index(2, 3, 5)
print(index)  # ValueError: 2 is not in list
```

* .count(x)

리스트에서 항목 x가 등장하는 횟수를 반환
```python
a_list = [1, 2, 3, 4, 4, 5]
print(a_list.count(4))  # 2

a_list = [1, 2, 3, 4, [4, 4, 5]]
print(a_list.count(4))  # 1

a_list = [1, 2, 3, 4, [4, 5]]
print(a_list.count([4, 5]))  # 1
```