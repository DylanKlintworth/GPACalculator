from GPACalculator import GPACalculator
from Course import Course
import pyinputplus as pyinp


class GPACalculatorDisplay:

    def __init__(self):
        self.gpacalc = GPACalculator()

    def menu_input(self):
        print("Welcome to GPA Calculator!\n")
        choice = pyinp.inputMenu(choices=['Enter Courses', 'View Courses', 'View GPA', 'Quit'], numbered=True)
        print()
        if choice == 'Enter Courses':
            self.enter_courses()
        elif choice == 'View Courses':
            self.read_courses()
            self.print_courses()
            self.menu_system()
        elif choice == 'View GPA':
            self.read_courses()
            self.print_gpa()
            self.menu_system()

    def enter_courses(self):
        isEntering = True
        while isEntering:
            print("Enter Course Details: Name, Credits, Grade (-1.0 for name to quit)")
            name = input("Enter Course Name: ")
            if name == "-1":
                break
            course_credits = pyinp.inputFloat(prompt="Enter the course credits (ex. 3): ", min=1, max=4)
            grade = pyinp.inputFloat(prompt="Enter the grade you received (ex. 4.0): ", min=0, max=4)
            course = Course(name, course_credits, grade)
            self.gpacalc.add_course(course)
        self.write_courses()
        self.menu_system()

    def write_courses(self):
        with open("grades.txt", mode='a', encoding='utf-8') as file:
            for i in self.gpacalc.courses:
                course = i
                name = str(course.get_name())
                course_credits = str(course.get_course_credits())
                grade = str(course.get_grade())
                file.write(name+","+course_credits+","+grade+ "\n")
        file.close()

    def read_courses(self):
        self.gpacalc.courses.clear()
        with open("grades.txt", mode='r', encoding='utf-8') as file:
            lines = file.readlines()
            for i in lines:
                course_info = i.split(',')
                name = course_info[0]
                course_credits = float(course_info[1])
                grade = float(course_info[2])
                course = Course(name, course_credits, grade)
                self.gpacalc.add_course(course)
        file.close()

    def print_courses(self):
        print("Courses:\n")
        for i in self.gpacalc.courses:
            print(i)
        print()

    def print_gpa(self):
        credits = self.gpacalc.get_course_credits()
        quality_points = self.gpacalc.get_quality_points()
        gpa = self.gpacalc.calculate_gpa()
        print(f"You have {quality_points} Quality Points and {credits} Course Credits \
        \n\nGPA = Quality points ({quality_points}) / Course Credits ({credits}) = {gpa} \
        \n\nYour GPA is {gpa}\n")

    def menu_system(self):
        self.menu_input()
