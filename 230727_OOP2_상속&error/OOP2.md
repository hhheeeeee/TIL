# 상속
* 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것 

* 상속이 필요한 이유
    1. 코드 재사용
        * 상속을 통해 기존 클래스의 속성과 메서드를 재사용할 수 있음
        * 새로운 클래스를 작성할 때 기존 클래스의 기능을 그대로 활용, 중복된 코드 줄일 수 있음
    2. 계층 구조
        * 상속을 통해 클래스들 간의 계층 구조 형성
        * 부모와 자식 클래스 간의 관계 표현, 더 구체적인 클래스 만들 수 있음
    3. 유지 보수의 용이성
        * 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 되므로 유지 보수 용이
        * 코드의 일관성 유지, 수정 필요한 범위 최소화
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'안녕, {self.name}')


class Professor(Person):

    def __init__(self, name, age, department):
        Person.__init__(self, name, age)
        self.department = department


class Student(Person):

    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa


p1 = Professor('박교수', 49, '컴공')
s1 = Student('김학생', 20, 3.5)

p1.talk() # 안녕, 박교수
s1.talk() # 안녕, 김학생
```
* super()
    * 부모 클래스의 메서드를 호출하기 위해 사용되는 내장 함수
    * 부모 클래스가 많은 상황에서 메서드를 가져오는 흐름 순서에 문제 없도록 자동 호출을 한다
    * 부모의 상속 순서 생각 안하고 super로 사용할 수 있도록
    * 상속이 많아지고 부모 클래스의 이름이 변했을 때 유연하게 대처 가능

* 다중 상속
    * 두 개 이상의 클래스를 상속받는 경우
    * 상속받은 모든 클래스의 요소를 활용 가능
    * 중복된 속성이나 메서드가 있는 경우 **상속 순서**에 의해 결정됨

```python
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'안녕, {self.name}')


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'


class Firstchild(Mom, Dad):
    dad_gene = Dad.gene

    def swim(self):
        return '첫째 수영'

    def cry(self):
        return '첫째 응애 '


baby1 = Firstchild('아가')
print(baby1.cry())  # 첫째 응애
print(baby1.swim())  # 첫째 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY
print(baby1.dad_gene)  # XY

print(Firstchild.mro())
# [<class '__main__.Firstchild'>, <class '__main__.Mom'>, <class '__main__.Dad'>, \
# <class '__main__.Person'>, <class 'object'>]
```
* mro()
    * Method Resulolution Order
    * 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    * 기존 인스턴스 -> 클래스 순으로 이름공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식클래스 -> 부모클래스로 확장



# 에러와 예외

* 버그
    * 소프트웨어에서 발생하는 오류 또는 결함
    * 프로그램의 예상된 동작과 실제 동작 사이의 불일치

* 디버깅 Debugging
    * 소프트웨어에서 발생하는 버그를 찾아내고 수정하는 과정
    * 프로그램의 오작동 원인을 식별하여 수정하는 작업
      1. pring 함수
      2. 개발 환경에서 제공하는 기능(breakpoint, 변수 조회)
      3. Python tutor(단순 파이썬 코드인 경우)
      4. 뇌 컴파일, 눈 디버깅

* 에러
    * 프로그램 실행 중에 발생하는 예외 상황
    1. 문법 에러 (Syntax Error)
      * 프로그램의 구문이 올바르지 않은 경우
        * Invalid syntax
        * assign to literal
        * EOL (End of Line)
        * EOF (End of File)
    2. 예외 (Exception)
      * 프로그램 실행 중에 **감지**되는 에러
      * 내장 예외 Build-in Exceptions
        * ZeroDivisionError
        * NameError
        * TypeError 인자 초과, 인자 타입 불일치
        * ValueError ex. int('1,5'), range(3).index(6)
        * IndexError
        * KeyError
        * ModuleNotFoundError
        * Import Error
        * KeyboardInterrpt
        * Indentation Error


# EAFP & LBYL
* try-except
    * 내장 예외 클래스는 상속 계층구조를 가지기 때문에 except절로 분기시 반드시 **하위 클래스를 먼저** 확인할 수 있도록 작성해야 함
[예외 계층 구조](https://docs.python.org/ko/3/library/exceptions.html#exception-hierarchy)

* EAFP : Easier to ask for Forgiveness than Permission
  * 예외처리를 중심으로 코드 작성(try-except)

* LBYL : Look Before You Leap
  * 값 검사를 중심으로 코들 작성 (if-else)

* as 키워드
  * as 키워드를 활용하여 에러메시지를 except블록에서 사용 가능
```python
my_list = []

try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생!!')
    # list index out of range가 발생!!
```