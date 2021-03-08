# values = [item * 2 for item in range(5) if item > 2]
# print(values)

try:
    age = int(input("Age: "))
except ValueError:
    print("Fuck you")
