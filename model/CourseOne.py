class CourseOne:
    def __init__(self,name,size,course_price):
        self.name = name
        self.__size = size
        self.__students = []
        self.course_price = course_price

    def add_student(self,student):
        if len(self.__students) < self.__size:
            self.__students.append(student)
            self.course_price = self.__calculate_course_price(student)
            print(f" Welcome {student.first_name} {student.last_name} You have successfully registered, please pay {self.course_price}")
        else:
            print("The course is full, you were not able to register")

    def print_students(self):
        for student in self.__students:
            student.print_student()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,size):
        self.__size = size

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self,students):
        self.__students = students

    def __calculate_course_price(self,student):
        if student.discount > 0:
            return self.course_price - student.discount
        else:
            return self.course_price
