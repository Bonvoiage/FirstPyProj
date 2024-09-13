class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f"Привет, меня зовут {self.name}")


class StudentGroup:
    def __init__(self, group):
        self.group = group
    
    def about(self):
        # print(f"{self.name} учится в  группе")
        print(f"{self.name} учится в {self.group} группе")


# class Student(Human, StudentGroup):
#     def __init__(self, name, place):
#         # Human.__init__(self, name)
#         super().__init__(name)
#         self.place = place
#         super().info()

# # human = Human("Denis")
# # print(human.name)
# student = Student("Max", "Moscow")
# # print(student.name, student.place)
# student.about()

# print(Student.mro())


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        # Human.__init__(self, name)
        super().__init__(name, group)
        self.place = place
        super().info()

student = Student("Max", "Moscow", "pyhton 03")
