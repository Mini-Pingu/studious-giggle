# Python3

> 2021年 周日計劃

1. 學習材料

   Mosh 的兩個 Python 課程

2. 原則

   和 Node.js 的原則一樣

3. 階段

   以每周周日全日時間爲一整次學習時長，爲其大概要2個月。在階段最後，最基礎要用 Django 來完成一下項目，和一個爬蟲項目。（共兩個項目）

4. 後續知識

   1. 爬蟲
   2. Django
   3. CUDA programming
   4. Unit Testing
   5. 裝飾器
   6. Generator

5. 要求

   1. 按照 `PEP8` 來規範代碼風格

6. 庫

   1. Anaconda
   2. pprint

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
