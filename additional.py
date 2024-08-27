grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
avgGrades = {}
number = 0
while len(grades) > number:
    avgGrades[students[number]] = sum(grades[number]) / len(grades[number])
    number += 1
print(avgGrades)
