import pyinputplus

class Course:
    
    def __init__(self, name, course_credits, grade):
        self.name = name
        self.course_credits = course_credits
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
        
    def get_course_credits(self):
        return self.course_credits
    
    def set_course_credits(self, course_credits):
        self.course_credits = course_credits

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def __str__(self):
        return f'Course Name: {self.name}, Course Credits: {self.course_credits}, Grade Received: {self.grade}'

