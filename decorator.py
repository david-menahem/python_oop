class Decorator:

    def __init__(self,name):
        self.name = name

    def say_goodbye(function):
        def wrapper(self):
            print("Goodbye")
            function(self)
        return wrapper

    @say_goodbye
    def say_hello(self):
        print("Hello " + self.name)

