from decorator import Decorator
from inheritance.chair.GamingChair import GamingChair
from inheritance.chair.KitchenChair import KitchenChair
from inheritance.chair.Parts import Parts
from inheritance.model.Bycycle import Bycycle
from inheritance.model.Car import Car
from model.CourseEnum import CourseEnum
from model.CourseOne import CourseOne
from model.Level import Level
from model.StudentOne import StudentOne
from model.Item import Item
from model.StudentTwo import StudentTwo


def print_course_register_count(students_list):
    for course in CourseEnum:
        count = 0
        for student in students_list:
            course_registered = student.course
            if course.value == course_registered.value:
                count += 1
        print(f'Course: {course.name} has {count} students')


def amount_registered(student_list):
    course_counts = {}
    for course in CourseEnum:
        course_counts[course.name] = 0
    for student in student_list:
        course_counts[student.course.name] = course_counts[student.course.name] + 1
    print(course_counts)


if __name__ == '__main__':
    # student and courses
    my_student = StudentOne("David", "Menahem", 38, "Ra'anana", "dvmena39@gmail.com", 2000)
    my_student_2 = StudentOne("Yael", "Menahem", 37, "Ra'anana", "yael@gmail.com", 3000)

    fullstack = CourseOne("Fullstack", 1, 19000)
    ai = CourseOne("AI", 15, 25000)
    fullstack.add_student(my_student)
    ai.add_student(my_student_2)
    ai.print_students()
    print()
    fullstack.print_students()

    # decorator
    david = Decorator("David")
    david.say_hello()

    # item
    router = Item('Router', 300, 'Computers', 5, 0.5)
    computer = Item('Computer', 1000, 'Computers', 10, 2)

    print(f'Item name: {router.name}, Item price: {router.price} NIS, Item category: {router.category}'
          f' Item amount: {router.amount}, Item weight: {router.weight} kg')

    router.name = "TP link router"
    router.price = 200
    router.category = "Electronic and internet"
    router.amount = 3
    router.weight = 1

    router.print_item(router)

    print(id([]))
    first_list = []
    second_list = []
    print(id(first_list))
    print(id(second_list))

    first = {1: "1", 2: '2', 3: "3"}
    second = {1: "1", 2: '2', 3: "3"}
    print(first == second)

    level = Level.LOW_LEVEL
    print(level.value)
    for level in Level:
        print(level.name)

    if isinstance(level, Level):
        print(level.value)

    # Enum
    first_student = StudentTwo('David', 'Menahem', 38, CourseEnum.PRODUCT_MANAGEMENT, "dvmena39@gmail.com")
    second_student = StudentTwo('Avi', 'Menahem', 38, CourseEnum.CYBER, "dvmena39@gmail.com")
    third_student = StudentTwo('Yael', 'Menahem', 38, CourseEnum.AI, "dvmena39@gmail.com")

    students = [first_student, second_student, third_student]

    print_course_register_count(students)
    amount_registered(students)

    # Class inheritance
    my_bycycle = Bycycle("Giant", "XR")
    my_car = Car("Ford", 'Fiesta')

    print(my_bycycle.brand)
    my_car.honk()

    # Chairs
    my_parts = Parts("black",50)
    my_chair = KitchenChair("X",4,500,False,False,True,25)
    my_chair.print_chair()
    print("The order amount is: " + str(my_chair.calculate_price(5)))
    my_chair.has_discount = False
    print("The order amount is: " + str(my_chair.calculate_price(5)))
    gaming_chair = GamingChair("x",1,500,True,True,True,25, my_parts)
    gaming_chair_copy = gaming_chair
    gaming_chair_copy.parts.screws = 60
    gaming_chair.print_chair()
