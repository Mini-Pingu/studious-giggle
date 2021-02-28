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

5. 要求

   1. 按照 `PEP8` 來規範代碼風格

6. 庫

   1. Anaconda

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

### 2021-02-28

#### 筆記

1. 創建 `def`

   ```python
   def func():
       print("func")
       
   
   func() # 打印出 func
   ```

   

#### 重點