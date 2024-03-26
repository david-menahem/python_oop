class StudentOne:

    def __init__(self, first_name: str, last_name: str, age: int, city: str, email: str, discount: float):
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
