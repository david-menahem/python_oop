from model.CourseEnum import CourseEnum


class StudentTwo:

    def __init__(self, first_name: str, last_name: str, age: int, course: CourseEnum, email: str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        if isinstance(course, CourseEnum):
            self.course = course
        self.email = email
