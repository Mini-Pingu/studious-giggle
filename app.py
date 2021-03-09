class Point:
    default_value = 10
    # 這個值是可以被任何的 class 或者 instance 獲取和修改
    # 會好危險

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)
        # 等於 Point(0, 0)

    def draw(self):
        print(f"{self.x}, {self.y}")
        print("draw")


point = Point(1, 2)
print(point.x)
print(point.y)
point.draw()
print(isinstance(point, Point))
print(Point.default_value)
print(point.default_value)

point = Point.zero()
# 可以使用 @classmethod 的方式
# 來減少輸入數值的麻煩
