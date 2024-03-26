from model.StudentOne import Student

if __name__ == '__main__':
    first_student = Student("David","Menahem",38,"Ra'anana","dvmena39@gmail.com",500)
    second_student = Student("David", "Menahem", 38, "Ra'anana", "dvmena39@gmail.com", 500)
    print(id(first_student))
    print(id(second_student))
    print(id(20))
    print(id(True))

    print()
    second_student = first_student
    print(id(first_student))
    print(id(second_student))

    first_student.first_name = "Yael"

    print(second_student.first_name)

    x = 50
    y = 50
    print(id(y))
    print(id(x))
def example():
    print("hello")

print(id(example))
print(type(example))

def add_to_list(list):
    list.append(2)
    return list


print(add_to_list([]))
print(add_to_list([]))