class Human:

    head = True
    _legs = True
    __arms = True

    def about(self):
        print(self.head, 
              self._legs, 
              self.__arms)
        

    def say_hello(self):
        print("Hello")


class Student(Human):
    arms = False 
    # def about(self):
    #     print("Я студент")


class Teacher(Human):
    
    def about(self):
        print("Я учитель")

human = Human()
# human.about()


student = Student()
# student.about()
# print(dir(Human()))
# print(dir(Student()))

print(student._Human__arms)

# # human = Human()
# student = Student()
# # print(student.head)
# # print(human.head)
# # student.about()