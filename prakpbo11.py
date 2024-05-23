import functools

class Person:
    def __init__(self, first_name, last_name, title, nim):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.nim = nim
        
    def display_info_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            full_name = func(self, *args, **kwargs)
            return f"Full Name: {full_name} {self.nim}"
        return wrapper
   
    @display_info_decorator
    def get_full_name(self):
        return f"{self.title} {self.first_name} {self.last_name}"

first_name = "Zahwa"
last_name = "Nur Azkia Putri"
title = "Mrs."
nim = "064002300038"

person = Person(first_name, last_name, title, nim)
print(person.get_full_name())