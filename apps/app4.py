def greet(first_name, last_name=1):
    print(f"{first_name}, {last_name}")


# greet("a", "b")
greet("a")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("hihi")
multiply(2, 3, 4, 5)


def save_user(**user):
    print(user)


save_user(id=1, name="chris")
