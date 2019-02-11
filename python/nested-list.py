def get_students_with_grade(students, grade):
    return list(filter(lambda student: student[1] == grade , students))

def get_second_lowest_grade(students):
    unique_grades = set(map(get_grade, students))
    ascending_grades = sorted(unique_grades)
    return ascending_grades[1] # return second lowest grade

def get_grade(student):
    return student[1]

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_lowest_grade = get_second_lowest_grade(students)
    students_with_grade = get_students_with_grade(students, second_lowest_grade)
    sorted_students = sorted(students_with_grade)
    for name, _score in sorted_students:
        print(name)
