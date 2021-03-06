successful = True

for number in range(10):
    print("hihi", number)
    if successful:
        print("fuck")
        break
else:
    print("hihihi")

for x in range(5):
    print("=" * 10)
    for y in range(3):
        print(f"({x}, {y})")
