from decorator import Decorator
from model.Course import Course
from model.Student import Student

if __name__ == '__main__':
    my_student = Student("David","Menahem",38,"Ra'anana","dvmena39@gmail.com",2000)
    my_student_2 = Student("Yael", "Menahem", 37, "Ra'anana", "yael@gmail.com",3000)

    fullstack = Course("Fullstack",1,19000)
    ai = Course("AI",15,25000)
    fullstack.add_student(my_student)
    ai.add_student(my_student_2)
    ai.print_students()
    print()
    fullstack.print_students()

    david = Decorator("David")

    david.say_hello()


