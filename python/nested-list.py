def get_students_with_grade(students, grade):
    return list(filter(lambda student: student[1] == grade , students))

def get_grade(student):
    return student[1]

def get_second_lowest_grade(students):
    grades = set(map(get_grade, students))
    ascending_grades = sorted(grades)
    return ascending_grades[1] # return second lowest grade

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grade = get_second_lowest_grade(students)
    # print("Grade {}".format(grade))
    students_with_grade = get_students_with_grade(students, grade)
    # print("Students with grade {}".format(students_with_grade))
    sorted_students = sorted(students_with_grade)
    for student in sorted_students:
        print(student[0])
