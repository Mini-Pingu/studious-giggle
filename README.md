# Python3

> 2021年 周日計劃

1. 學習材料

   Mosh 的兩個 Python 課程 （Python Develop 版只是 Django 更多一些，可以直接看 Developer 版的 Djangos）

2. 原則

   和 Node.js 的原則一樣

   因爲 Mosh 這個課程是2018年的，所以只能是有他提及的概念，再去尋找該概念最新的技術，而不能直接用他提及的庫或者工具。

3. 階段

   以每周周日全日時間爲一整次學習時長，爲其大概要2個月。在階段最後，最基礎要用 Django 來完成一下項目，和一個爬蟲項目。（共兩個項目）

   2021-03-14: 中途插入 [12個新手項目](https://www.youtube.com/watch?v=8ext9G7xspg)

4. 後續知識

   1. 爬蟲
   2. Django
   3. CUDA programming
   4. Unit Testing
   5. 裝飾器
   6. Generator
   7. 看 python 官方文檔
   8. class

5. 要求

   1. 按照 `PEP8` 來規範代碼風格

6. 庫

   1. Anaconda
   2. pprint
   3. timeit

7. 目的

   1. 規範自己的 python 代碼

8. 有用 website

9. VS Code 相關

   1. extension
      1. pylint
      2. `autopep8`
      3. code runner => `ctl` + `alt` + `n` 自動運行代碼（記得更改 code runner 的 ` "code-runner.executorMap": {"python" : "python3 -u"}`）
   2. `shift` + `ctrl` + `M` => 顯示 Problems 版面
   3. `shift` + `ctrl` + `P` => 顯示 control 選擇版面
   
10. 注意

    1. Mosh 的課程太舊了，需要更新的地方有很多。。。

## Complete Python Mastery

## Getting Started

### 2021-02-28

#### 筆記

1. 只學習 python3

#### 重點

1. 爲了方便，創建合適的 Code snippets

## Primitive Types

### 2021-02-28

#### 筆記

1. 命名需要有意義，長不要緊。

#### 重點

1. `python` 用 `_` 來命名

2. String 合一起用 `f""`

   ```python
   first = "a"
   last = "b"
   full = f"{first} {last}" # 比 full = first + " " + last
   ```

3. 熟悉 String 的各種 method

4. `10 // 3 -> 3` 不同與 `10 / 3 -> 3.3333`

## Control Flow

### 2021-02-28

#### 筆記

1. 雖然 `python` 的 `if` statement 是短路機制，不過對比下來，對運行時間上的影響不大。 

#### 重點

1. 極簡判斷 if - else

   ```python
   age = 2
   message = "hihihi" if age > 19 else "ijijiji"
   print(message) # ijijiji
   ```

2. `if` 中的 `and` `or` `not` 是爲了判斷 `True` 和 `False` 的值

3. 以下語法是正確的

   ```python
   if 18 <= age < 65:
   	print("hihi")
   ```

4. 所有 `range()` 的 `index` 都必須是從 0 開始，不能改變

5. ***`For - else` => 這個很重要***

   ```python
   successful = True
   
   for number in range(10):
       print("running @ ", number)
       if successful:
           print("successful")
           break
   else:
       print("failed after running 10 times")
   ```

6. 全部用 `f"{var}"` 方式來 `print`

## Functions

### 2021-03-02

#### 筆記

1. 創建 `def`

   ```python
   def func():
       print("func")
       
   
   func() # 打印出 func
   ```


#### 重點

1. 最好是直接 `return` ，而不是 `print`

   ```python
   def greet(name):
   	print(f"{name}")
   	
   def get_greet(name)
   	return f"{name}" # 這種更好
   ```

2. 寫 `function` 的良好習慣

   ```python
   def increment(number, by):
   	return number + by
   	
   print(increment(number=2, by=1)) # 要在每個 function 的 args 前加上名稱
   
   #=========
   
   def increment2(number2, by2 = 1): # by2 = 1 預設值
       return number + by
   
   print(increment2(3))
   ```

3. 如果不確定 `args` 的個數（屬性是 `list`），要加星

   ```python
   def multiply(*numbers):
   	print(numbers)
   	
   multiply(1, 2, 3) # print => (1, 2, 3) tuple
   ```

4. 如果 `args` 是 dictionary，要加雙星

   ```python
   def multiply(**user):
   	print(user)
   	print(user["name"])
   	
   multiply(id=1, name="chris", age=22)
   ```

5. 不可以直接在 `function` 裏直接使用 `global variable`

6. ***使用 VS Code 的 Debugger: `lanuch.json` 來 debug***

## Data Structures

### 2021-03-05 && 06 && 08

#### 筆記

1. `list` 裏放什麼都行，不同數據類型一起放也行
2. 使用 `enumerate()`  可以獲取元素和序號

#### 重點

1. 可以使用一下方法來創建 `list`:

   ```python
   zeros = [0] * 100
   print(zeros) # [0,0,0,....]
   ```

2. 也可以這樣子來創建 `list`:

   ```python
   numbers = list(range(20))
   print(numbers)
   # [0, 1, 2, 3, ... 20]
   ```

3. 可以用 `list()` 來 loop 字符串

   ```python
   chars = list("hello world")
   print(chars)
   # ["h", "e", ...]
   ```

4. 可以用 `[::step number]` 來跳數

   ```python
   chars = list("Hello world")
   print(chars[::2])
   ```

5. 可以用 `[::-1]` 來倒數

   ```python
   chars = list("Hello world")
   print(chars[::-1])
   ```

6. 可以用以下方式來取數

   ```python
   chars = list("Hello world")
   first, second, *other, last = chars
   print(first)
   print(second)
   print(other)
   print(last)
   ```

7. 刪除元素

   ```python
   letters = ["a", "b", "c"]
   
   # 幾種刪除 list 元素的方法
   letters.pop(0)
   letters.remove("b")
   del letters[0:3]
   letters.clear()
   ```

8. 元素排序

   ```python
   tuple_listing = [
       ("a", 1),
       ("b", 3),
       ("c", 2)
   ]
   
   tuple_listing.sort(key=lambda item: item[1])
   print(tuple_listing)
   # [('a', 1), ('c', 2), ('b', 3)]
   
   number_list = list(map(lambda item: item[1], tuple_listing))
   print(number_list)
   # [1, 3, 2]
   # 要知道 lambda 的用法
   ```

9. 元素過濾

   ```python
   tuple_listing = [
       ("a", 1),
       ("b", 3),
       ("c", 2),
       ("d", 20)
   ]
   
   filtered = list(filter(lambda item: item[1] >= 10, tuple_listing))
   print(filtered)
   ```

10. ***要活用 `map()` 和 `filter()` 函數，類似 javascript。會大大提升代碼可讀性。***

11. python3 特有的更加直觀方法

    ```python
    number_list = list(map(lambda item: item[1], tuple_listing))
    number_list = [item[1] for item in items]
    print(number_list)
    
    filtered = list(filter(lambda item: item[1] >= 10, tuple_listing))
    filtered = [item for item in items if item[1] >= 10]
    print(filtered)
    ```

12. `zip()` 可以將兩個 `list` 合在一起。

13. 要好好學學  python3  的`collections` 模塊用法

14. ***`0`, `null` ,`[]` 都系 falsy 值，所以可以用 `not` 來處理，譬如***

    ```python
    if not 0: # if ture
    if not null: # if ture
    if not []: # if ture
    ```

15. 交換數值

    ```python
    x = 10
    y = 11
    x, y = y, x
    print(x, y) # 11, 10
    ```

16. ***使用 `array` 庫來限定 `python` 的 `array` 類型或者其他屬性，可以縮小程序運行時間。***

    ***要睇 `array` 庫的用法！！！！***

17. `set` 可以用來除去重復的項，不同 `set` 之間有不同的組合用法

    ***要睇 `set` 庫的用法！！！！***

18. `dict()` 的用法

    ```python
    point = dict(x=1, y=2)
    point["x"] = 10
    point["z"] = 20
    print(point.get("a", 0)) # 獲取 key 爲 a 的值，如果沒有就返回 0
    del point["x"] # 去除 key 爲 x 的 key-value pair
    for key, value in point.items():
        print(key, value)
    ```

19. 要多用 comprehensions

    ```python
    # [expression for item in items if item > 2 ]
    values = [item * 2 for item in range(5) if item > 2]
    print(values) # [6, 8]
    # 也可以用 [], {} 來裝這些 for in if 產出的東西 
    ```

20. 用 `{}` 來裝的東西，如果只有 單個值的話，就是 `set` ；如果是 `key-value pair` 的話，就是 `dict`

21. 可以使用 `*list` 來 unpack `list` 裏的內容，也可以使用 `**dict` 來 unpack  `dictionary` 裏的內容。

## Exceptions

### 2021-03-08 && 09

#### 筆記

#### 重點

1. 最重要的一點是：

   exception 會拖慢效率，要考慮是否真的要 exception

2. 常規流程

   ```python
   try:
       age = int(input("Age: "))
   except ValueError as error:
       print("You entered the wrong type value.")
       print(error)
       print(type(error))
   else:
       print("當 try 和 except 都出錯的時候，就到這裏")
   print("try except 完了之後，就會打印這個。")
   ```

3. 兩個重復 `print` 的 `except` 的格式

   ```python
   try:
       age = int(input("Age: "))
       x = 10 / age
   except (ValueError, ZeroDivisionError):
       print("You entered the wrong type value.")
   else:
       print("hihi")
   ```

4. 完成的格式

   ```python
   try:
   	print("hihi")
       # 當 try 中的某一行除了 error 的話
       # 就會直接跳過剩下的 code
       # 去到 except
   except:
       print("hihihi")
   else:
       print('hihihihih[]')
   finally:
       print("無論如何都會執行這行")
   ```

5. 可以同時 `with open`  兩個文件

   ```python
   with open("one.txt") as one_file, open("two.txt") as two_file:
   	print(one_file)
   	print(two_file)
   ```

6. 可以手動 `raise error`

   ```python
   def function(age):
   	if age <= 0:
   		raise ValueError("hihihi")
   	return 10 / age
   
   try:
       function(-1)
   except ValueError as error:
       print(error)
   ```

## Classes

### 2021-03-14 (一次過學完)

#### 筆記

1. Class: Blueprint for creating new objects => Human

2. Object: instance of a class => John

3. Class 命名規則：MyPoint

4. Class 自身的內部使用的變量需要 `constructors` 來創建

5. ***Properties 這一節，有些不懂***

6. 繼承

   ```python
   class Animal:
       def __init__(self):
           self.age = 1
   
       def eat(self):
           return "eat"
   
   
   class Mammal(Animal):
       def walk(self):
           return "walk"
   
   
   m = Mammal()
   print(m.age)
   print(m.walk())
   print(m.eat())
   ```

7. 可以用 `abc` 庫來規範 `class` 的用法，具體還要再仔細看那個 庫 的用法

#### 重點

1. 這片文章對 `class` 的用法有很詳細的講解：[A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/)

2. `class` 就好似將 `list`, `dictionary`, `set` 這類的最基礎的數據結構再做一次封裝。

3. 可以使用 `isinstance()` 來判斷某個 `object` 是否由 某個 `class` 來創建的：

   ```python
   point = Point()
   pring(type(poing))
   print(isintance(point, Poing)) # True
   ```

4. 使用 `constructor` 可以用來接受 傳給 `class` 的變量，並在 `class` 內部使用

   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y
   
       def draw(self):
           # print(f"Point ({self.x}, {self.y})")
           # return "draw"
           return f"Point ({self.x}, {self.y})"
   
   
   point = Point(1, 2)
   print(point.x)
   print(point.y)
   print(point.draw())
   
   ```

5. `class` 的通用 `variable` 可以被全部的 `instance` 使用

   ```python
   class Point:
       class_variable = 10
       def __init__(self, x, y):
           self.x = x
           self.y = y
           
   point_a = Point(1, 2)
   point_b = Poing(2, 3)
   print(point_a.class_variable) # 10
   print(point_b.class_variable) # 10
   print(Point.class_variable) # 10
   
   Point.class_variable = 20
   # 這個 Point Class 的 class variable 可以被修改
   # 這個是比較危險的
   ```

6. 當需要創建比較復雜的 `instance` 的時候，可以用以下方式來優雅地創建

   ```python
   class Point:
   	def __init_-(self, x, y):
           self.x = x
           self.y = y
           
       @classmethod
       def zero(cls):
           return cls(0, 0)
       
   point = Point.zero() # = point = Poing(0, 0)
   ```

7. Class 的 Magic Method 就是一些 Class 初始化就會附帶的 method，如果不用的話，就會浪費了。媽的。用起來。比較兩個 `instance` 是否一樣，要用 `__eq__` 來做。不然只是直接比較兩個 `instance` 的 `reference` 地址，會肯定不一樣。

   ```python
   class Point:
       def __init__(self, x, y):
           self.x = x
           self.y = y
           
       def __eq__(self, other):
           return self.x == other.x and self.y == other.y
   
       
   point_a = Point(1, 2)
   point_b = Point(1, 2)
   print(point_a == point_b) # True
   # 如果沒有 __eq__ 的設定，就一定是 False，因爲只是比較兩個 instance 的 內存地址
   # 這樣子就沒有意思了。
   ```

8. Magic Method 的意義就在於，可以將一些常用的 表達式，在 `Class` 裏特殊處理之後，就能更符合自身需要來使用。

9. `Class` 通過 `Magin Method` 來正常和外界溝通，再通過 `method` 來和 `list`, `set`, `dict` 自身的性質來進行數據處理和存儲。只要在任意變量前加上 `__` 就不可以被外界直接訪問了。

   一個例子：

   ```python
   class TagCloud:
       __default = "red"
   
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
   
   
   cloud = TagCloud()
   print(TagCloud.default)
   print(cloud["python"])
   cloud.add("Python")
   cloud.add("python")
   cloud.add("c")
   cloud.add("python")
   cloud["python"] = 10
   cloud.add("Python")
   print(cloud["python"])
   print(cloud["python"])
   
   for tag in cloud:
       print(tag)
   ```

10. 當 subclass 有自己的 `constructor` ，就要用 `super().__init__() ` 才能在 subclass 裏使用 parent 的 `constructor`, 不然的話，subclass 的 `constructor` 就會直接整個覆蓋了 parent 的  `constructor`

    ```python
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
    
    
    m = Mammal()
    print(m.age)
    print(m.walk())
    print(m.eat())
    print(m.weight)
    print(m.age)
    ```

11. ***繼承關系的 class 最多就只有 2 層，不然會很容易出問題***

12. 可以在一個 `class` 裏繼承兩個 `class`，可是當兩個 parent 有同樣命名的 function 時，執行的順序就會按照加載 `class` 的順序來進行

    ```python
    class A:
        def greet(self):
            return "A"
    
    
    class B:
        def greet(self):
            return "B"
    
    
    class C(B, A):
        pass
    
    
    c = C()
    print(c.greet()) # "B"
    
    ```

13. `class` 可以繼承 基礎數據類型

    ```python
    class Text(str):
        def duplicate(self):
            return self + self
    ```

## Modules

#### 2021-03-14

#### 筆記

1. python 比 javascript 方便的地方在與，可以不用 export 就可以使用其他 modules 的 method。

#### 重點

1. 不要使用 `import * from modules`， 因爲會導致 `method override`。要用哪個才拿哪個。

2. 也可以使用 `import modules`，再在剩下的內容中使用 `modules.method` 來使用該 `method`

3.  可以引用其他文件夾裏的 `py` 文件

   - 文件架構

   ```bash
   .
   ├── app.py
   └── ecommerce
       ├── __init__.py
       └── sales.py
   ```

   - 一定要加 `__init__.py` 在文件夾裏

   - `app.py`

     ```python
     from ecommerce.sales import calc_tax, calc_shipping
     from ecommerce import sales
     
     calc_shipping()
     calc_tax()
     ```

   - `sales.py`

     ```python
     def calc_tax():
         print("calc_tax")
     
     
     def calc_shipping():
         print("calc_shipping")
         
     ```

4. 可以通過 `dir()` 來觀察不同 modules 的屬性

5. 作爲`Module` 和單獨執行的區別

   ```python
   # 如果單獨執行的話， __name__ == "__main__"
   if __name__ == "__main__":
       main()
       
   # 如果是其他文件 import 的話，__name__ not == __main__，
   # 而是 該 import 文件的路徑全稱
   ```

## Python Standard Library

### 2021-03-14

#### 筆記

1. 提到的有用的庫
   1. `pathlib`
   2. `glob` 和 `rglob`
   3. `shutil`
   4. `zipfile`
   5. `csv`
   6. `json`
   7. `sqlite3`
   8. `time`
   9. `datetime`
   10. `random`
   11. `string`
   12. `smtp`
   13. `sys`
   14. `subprocess`

#### 重點

1. 任何需要對文件進行處理，最好用

   ```python
   with open("file") as file:
   	# ...
       
   with sqlite3.connect("db") as conn:
       # ...
   ```

## Python Package Index

### 2021-03-14 && 15

#### 筆記

1. 可以通過上傳自己開發的 package 到 pypi 上
2. 可用的庫
   1. `requests`
3. 和 `node.js` 的 `npm` 差不多
4. 可以發布自己的 `package` 到 `pypi`

#### 重點

1. 使用 `anaconda`，作爲環境工具

2. `pipenv` 就像 `npm` 

3. 要對自己程序的每一個 `class` 和 `function` 都要 well-documented，不只是 `python` ，`javascript` 都系

   ```python
   class PDF2Text:
       """
      	this is a short summary about this class
      	
      	more details...
       """
       def pdf2text(self, path):
           """
           This is a short summary of this funtion
           
           more details...
           
           Parameters:
           path (str): The path to a PDF file.
           
           Returns:
           str: The content of the PDF file as text.
           """
           print("pdf2text")
   ```

4. 要爲自己的項目，怎樣都要加一個 [licence](https://choosealicense.com/)。

5. 在項目根目錄下 執行 `pydoc3 -p [port]`，可以查看到該 項目下所有的 documentaion. 

## Popular Python Packages

### 2021-03-15 && 16

#### 筆記

1. 爬蟲用 `scrapy`， 不要用 `bs4`

2. `selenium` 做自動化

3. 可以簡化 `import` 的 module

   ```python
   import numpy as np
   ```

#### 重點

1. 要留意每一個網站的 api 設計理念
   1. yelp
   2. github
2. 發送信息可以使用 twilio 服務
3. 重要保密內容要分來，用 `.gitignore` 來避免上傳
4. ***`assert` 用法***

## Building Web Applications with Django（取第二部分 教程）

### 2021-03-16 && 17

#### 筆記

1. sqlite 只適合移動小應用使用
2. `django` 可以有自己的後端（後臺），前端渲染引擎，可以加第三方提供 api，不過太重了。

#### 重點

1. 不要刪除任意 `APP` 的 `migration`