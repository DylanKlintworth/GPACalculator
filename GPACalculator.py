class GPACalculator:

    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def add_courses(self, courses):
        self.courses.extend(courses)

    def get_quality_points(self):
        quality_points = 0
        for i in self.courses:
            quality_points = quality_points + (i.get_course_credits() * i.get_grade())
        return quality_points

    def get_course_credits(self):
        course_credits = 0
        for i in self.courses:
            course_credits += i.get_course_credits()
        return course_credits

    def calculate_gpa(self):
        quality_points = self.get_quality_points()
        course_credits = self.get_course_credits()
        gpa = quality_points / course_credits
        return gpa

