class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

        def get_grade(self):
            return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.maxstudents = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.maxstudents:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        pass


s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Kent", 19, 65)

course1 = Course("Computer Science", 2)
course1.add_student(s1)
course1.add_student(s2)

for student in course1.students:
    print(student.name)

