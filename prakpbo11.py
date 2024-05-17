def full_name_decorator(func):
    def wrapper(first_name, last_name, title, nim):
        full_name = func(first_name, last_name, title)
        return f"Full Name: {full_name} {nim}"
    return wrapper

@full_name_decorator
def format_name(first_name, last_name, title):
    return f"{title} {first_name} {last_name}"

# Contoh penggunaan
first_name = "Zahwa"
last_name = "Nur Azkia Putri"
title = "Mrs."
nim = "064002300038"

print(format_name(first_name, last_name, title, nim))
