# []中括號 是陣列
list = ["apple", "banana", "cherry", "apple"]
print(list)
print(list[0]) #陣列一率重0開始
print(list[1])

list[3] = "mango"
print(list)
list.remove("banana") #比較數值，一樣才會移除
print(list)
del list[1] #指定第幾個位子的刪除
print(list[1])


list.append("orange") #在最後一個位置添加
list.append("papaya")
print(list)

list.insert(1, "peach") #指定位置添加
print(list)

list.sort() #重新排列，變數必須要是同一個類別才行，像是數值或文字
print(list)

list.reverse()
print(list)

print(len(list))



list2 = ["car", "truck", "airplane"]

list3 = list + list2 #列的合併
print(list + list2)

list3.sort()
print(list3)


#===== list + list2=====

print("=" * 30)
print(list)
print(list2)
list3 = list + list2
print(list3)
print("=" * 30)