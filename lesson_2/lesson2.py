# 算術運算子 (Arithmetic Operators)
num1 = 76
num2 = 60

# 模除運算子 (%)：計算除法後的餘數
# 76 除以 60 的餘數是 16
print(num1 % num2)


# 複合賦值運算子 (Assignment Operators)
x = 5 
x += 3 # 等同於 x = x + 3，此時 x 變為 8
print(x) # 輸出 8

print("======")
x = 5
x - 3 # 這行僅計算了 5 - 3，但沒有將結果存回變數，所以 x 的值依然是 5
print(x - 3) # 輸出 2 （僅列印計算結果，不改變 x 的值）
print(x) # 輸出 5
x = x - 3  # 也可以寫成 x -= 3，將 x 的值減 3 後存回 x，此時 x 變為 2
print(x) # 輸出 2


#===========
print("======")

# 比較運算子 (Comparison Operators)
# 一個等號 (=) 是「變數的指派/賦值」
# 兩個等號 (==) 是「比較兩個值是否相等」
x = 5
y = 3

print(x == y) # 檢查 x 是否等於 y -> False
print(x != y) # 檢查 x 是否不等於 y -> True
print(x > y)  # 檢查 x 是否大於 y -> True
print(x < y)  # 檢查 x 是否小於 y -> False
print(x >= y) # 檢查 x 是否大於或等於 y -> True
print(x <= y) # 檢查 x 是否小於或等於 y -> False


#===========
print("======")

# 邏輯運算子 (Logical Operators)
# and => 且/和（左右兩邊皆為 True 時，結果才為 True）
# or  => 或（左右兩邊只要其中一個為 True，結果就為 True）
# not => 非/相反（反轉布林值，True 變 False，False 變 True）

x = 10
print(x > 5 and x < 15) # 10 > 5 為 True，且 10 < 15 為 True -> True 
print(x > 8 or x < 3)   # 10 > 8 為 True，或 10 < 3 為 False -> True
print(not x > 5)        # 10 > 5 為 True，加上 not 後反轉為 False
print(x > 3)            # 10 > 3 為 True -> True


print("======")
# 成員運算子 (Membership Operators)
# list 是一個串列/清單
list = ["apple", "banana", "cherry", "apple"]
print("cherry" in list) # 檢查 "cherry" 是否在 list 清單中 -> True
print("melon"  in list) # 檢查 "melon" 是否在 list 清單中 -> False
print(list)


