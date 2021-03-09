# values = [item * 2 for item in range(5) if item > 2]
# print(values)

try:
    age = int(input("Age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("You entered the wrong type value.")
else:
    print("hihi")
