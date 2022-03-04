class Student:
    def __init__(self, name, age, phone_num, form, subjects, is_male):
        self.name = name
        self.age = age
        self.phone_num = phone_num
        self.form = form
        self.subjects = subjects
        self.is_male = is_male
        self.enrolled = True

        student_list.append(self)

    def display_info(self):

        print("Name: {}\n"
              "Age: {}\n"
              "Phone Number: {}\n"
              "Form Class: {}\n"
              "Subjects: {}\n"
              "Enrolled: {}".format(self.name, self.age, self.phone_num, self.form, self.subjects, self.enrolled))

        if self.is_male == True:
            print("Gender: M")
        else:
            print("Gender: F")
        print("######################")


student_list = []
Student("Caleb", 17, "02041808817", "WNBH", ["Stats", "DTC", "Economics", "Physics"], True)
Student("Kento", 16, "0800838383", "WNNL", ["Physics", "DTC", "Calculus", "Chemistry"], True)
Student("Natasha", 15, "021461310", "SCED", ["Calculus", "DTC", "Economics"], False)
Student("Jack", 18, "021456789", "SKCG", ["DTC", "Building", "Drama"], True)


def show_students():
    for student in student_list:
        student.display_info()


def select_student_age():
    age = int(input("Please enter the minimum age of students you want to search for:"))
    for student in student_list:
        if student.age >= age:
            student.display_info()


select_student_age()
