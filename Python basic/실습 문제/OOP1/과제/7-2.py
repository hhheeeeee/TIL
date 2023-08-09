# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
    # def __init__(self):
    #     self.repeat = 0
    #     self.string = ""
    
    def repeat_string(self, repeat, string):
        for i in range(repeat):
            print(string)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
