grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
avg0 = sum(grades[0]) / len(grades[0])
avg1 = sum(grades[1]) / len(grades[1])
avg2 = sum(grades[2]) / len(grades[2])
avg3 = sum(grades[3]) / len(grades[3])
avg4 = sum(grades[4]) / len(grades[4])
d = dict(((students[0], avg0), (students[1], avg1), (students[2], avg2), (students[3], avg3), (students[4], avg4)))
print(d)

