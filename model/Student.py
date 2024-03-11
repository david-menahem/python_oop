class Student:

    def __init__(self,first_name,last_name,age,city,email,discount):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
        self.discount = discount


    def print_student(self):
        print(f" Student: {self.first_name} {self.last_name}")
        print(f"Age:  {str(self.age)}")
        print(f"city: {self.city}")
        print(f"{self.email}")

