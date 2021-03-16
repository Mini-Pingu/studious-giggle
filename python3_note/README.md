# python 避雷

## 來源

[5 Things You're Doing Wrong When Programming in Python](https://www.youtube.com/watch?v=fMRzuwlqfzs)

1. 一定要用 `if __name__ == "__main__"`，原因是方便文件被其他人導入，或者自己運行

   ```python
   if __name__ == "__main__":
   	main()
   ```

2. 爲了可以 用 `ctl + c` 來退出 py，一定到加上 `Exception`

   ```python
   import time
   
   while True:
       try:
           print("hihi")
           time.sleep(0.1)
       except Exception:
           print("hihihihi")
   ```

   