class Human:

    def __init__(self):
        self.about()

    head = True

class Student(Human):
    
    head = False
    def about(self):
        print("Я студент")

# human = Human()
student = Student()
# print(student.head)
# print(human.head)
# student.about()