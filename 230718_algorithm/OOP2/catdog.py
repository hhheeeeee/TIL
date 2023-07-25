class Animal:
    num_of_animal = 0
    
    def __init__(self):
        Animal.num_of_animal += 1

class Dog(Animal):
    def bark(self):
        print('멍멍!')

class Cat(Animal):
    
    def meow(self):
        print('야옹!')

# make_sound() : Pet 인스턴스 변수 sound를 출력한다
class Pet(Dog, Cat):

    def __init__(self, sound):
        self.sound = sound

    def play(self):
        print("애완동물과 놀기")
    
    def make_sound(self):
        print(self.sound)
    


pet1 = Pet("그르르")
pet1.make_sound()
pet1.bark()
pet1.meow()
pet1.play()
