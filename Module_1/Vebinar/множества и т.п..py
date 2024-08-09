# # a=[1,2,3,4]
# a=[]
# a.append("werty")
# print(a)

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# listed_students = list(students)
# stu_list = { listed_students[0] : sum(grades[0])/len(grades[0]) ,
#              listed_students[1] : sum(grades[1])/len(grades[1]) ,
#              listed_students[2] : sum(grades[2])/len(grades[2]) ,
#              listed_students[3] : sum(grades[3])/len(grades[3]) ,
#              listed_students[4] : sum(grades[4])/len(grades[4])
# }
# print(stu_list)
# students_sorted = sorted(stu_list, reverse=True)
# print(students_sorted)
#
# a = zip(students, grades)
# print(a)
# b = dict(zip(students, grades))
# print(b)
students_sort = sorted(students)
grades_m = []
for num in grades:
    s = sum(num)/len(num)
    grades_m.append(s)
b = dict(zip(students_sort, grades_m))
print(b)
