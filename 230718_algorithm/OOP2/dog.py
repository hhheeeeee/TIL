# ws_8_2.py

class Animal:
    num_of_animal = 0
    
    def __init__(self):
        Animal.num_of_animal += 1


# 아래 클래스를 수정하시오.
class Dog(Animal):

    def __init__(self, str):
        self.str = str

    def bark(self):
        print(self.str)

dog1 = Dog("멍멍")
dog1.bark()
