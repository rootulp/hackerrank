from collections import namedtuple


number_of_students = int(input().strip())
column_names = input().strip().split()
student = namedtuple('student', column_names)
students = []

for i in range(number_of_students):
    students.append(student(*input().strip().split()))

sum_of_all_marks = sum([int(student.MARKS) for student in students])
average = sum_of_all_marks / number_of_students
print(average)
