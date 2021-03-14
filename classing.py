class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        # print(f"Point ({self.x}, {self.y})")
        # return "draw"
        return f"Point ({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


# point = Point(1, 2)
# point.z = 10
# print(point.x)
# print(point.y)
# print(point.z)
# print(point.draw())

# print(isinstance(point, Point))

# point_zero = Point.zero()
# print(point_zero.y)
# print(point_zero.x)

# print(point)

# point_a = Point(1, 2)
# point_b = Point(1, 2)
# print(point_a == point_b)

class TagCloud:
    default = "red"

    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


# cloud = TagCloud()
# print(cloud.__dict__)
# print(TagCloud.default)
# print(cloud["python"])
# cloud.add("Python")
# cloud.add("python")
# cloud.add("c")
# cloud.add("python")
# cloud["python"] = 10
# cloud.add("Python")
# print(cloud["python"])
# print(cloud["python"])
# # print(cloud.__tags)
# print(cloud.__dict__)
# print(cloud._TagCloud__tags)

# for tag in cloud:
#     print(tag)

class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Fuck")
        self.__price = value

    price = property(get_price, set_price)


# product = Product(10)
# print(product.get_price())
# product.price = 1
# print(product.price)


# class Product2:
#     # def __init__(self, price):
#     #     self.__price = price
#     def __init__(self):
#         self.__price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Fucking")
#         self.__price = value


# product2 = Product2()
# product2.price = -1

class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        return "eat"


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.weight = 2

    def walk(self):
        return "walk"


# m = Mammal()
# print(m.age)
# print(m.walk())
# print(m.eat())
# print(m.weight)
# print(m.age)

class A:
    def greet(self):
        return "A"


class B:
    def greet(self):
        return "B"


class C(B, A):
    pass


c = C()
print(c.greet())
