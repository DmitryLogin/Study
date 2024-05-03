
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_1 = list(students)
students_2 = sorted(students_1)

grades_1 = []
for i in grades:
    a = sum(i) / len(i)
    grades_1.append(a)


students_and_grades = dict(zip(students_2, grades_1))

print(students_and_grades)
