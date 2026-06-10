# 宣告變數 a，並給予整數值 11
a = 11
# 宣告變數 b，並給予整數值 26
b = 26
# 宣告變數 name，並給予字串值 "gigi"
name = "gigi"
# 宣告變數 married，值為布林值 True (布林值只有 True 或 False 兩種)
married = True # only true or false

# 印出目前變數 b 的值 (為 26)
print(b)
# 將變數 b 重新賦值為整數 10
b = 10
# 將變數 name 重新賦值為字串 "andy"
name = "andy"
# 印出更新後變數 b 的值 (為 10)
print(b)
# 印出目前變數 b 的資料型態 (結果為 <class 'int'>)
print(type(b))

# 將變數 b 重新賦值為字串 "andy" (此時變數型態轉變為字串)
b = "andy"

# 印出變數 b 的資料型態 (結果為 <class 'str'>)
print(type(b))

# 宣告整數變數 a1，值為 1
a1 = 1
# 宣告字串變數 a2，值為 '1'
a2 = '1'

# 比較 a1 的型態 (int) 與 a2 的型態 (str) 是否相同，並印出布林結果 (結果為 False)
print(type(a1) == type(a2))

# False 是 Python 的保留字 (不能用來當變數名稱)，但 False_ 有底線，因此可以作為變數名稱
False_ = 1

# Python 的變數名稱大小寫敏感 (Case-sensitive)
# age, Age, AGE 在 Python 中是三個完全不同的變數
age = 10
Age = 11
AGE = 12

# 印出這三個不同變數進行數學運算後的值
print(age + 1)  # 10 + 1 = 11
print(Age + 2)  # 11 + 2 = 13
print(AGE + 3)  # 12 + 3 = 15

# 變數命名的風格範例 (說明 Python 與 Java 的常用風格)
# 駝峰式命名法 (Camel Case)，常用於 Java
# lastName # java
# 蛇形命名法 (Snake Case)，Python 推薦的命名風格
# last_name # python



# 將整數 age 透過 str(age) 轉換為字串，以便與 name 進行字串拼接印出 (在 Python 中不同型態直接相加會報錯)
print(name + ":" + str(age))
# 透過 int() 將 married 變數強制轉換為整數型態並印出 (此處已是整數 1)
print(int(married))