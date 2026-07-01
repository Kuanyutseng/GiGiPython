#一般迴圈
for i in range(3): # range(3) => [0,1,2]
    print(i)


# 巢狀迴圈
for i in range(3): # range(3) => [0,1,2]
    for j in range(3):
        if j == 2:
            #我不要輸出 j == 2 的結果，使用 continue 跳過本次迴圈
            num = (i + 1) * (j + 1)
            print(str(i + 1) + "*" + str(j + 1) + "=" + str(num))


# = 變數的宣告
# == 判斷相等
# != 不等於


pets = ["bird", "dog", "cat"]
for pet in pets:
    print(pet)



name = "gigilee" 
for char in name: #['g','i','g','i','l','e','e']
    print(char)


print("=" * 30)

# break 會中斷整個迴圈
# 這裡會先打印，再判斷是否要結束迴圈
for i in range(3):
    print(i)
    if i == 1:
        break

print("=" * 15) 

# 這裡會判斷是否要結束迴圈，再打印
for i in range(3):
    if i == 1:
        break # 結束迴圈
    print(i)



print("=" * 15)

for i in range(5):
    if i == 2:
        continue #跳過 這一次的迴圈 後面一樣會繼續執行
    print(i)

print("=" * 30)    




        # exmaple
        # save_list = []
        # available_value = ["store_name", "store_address", "store_email" ]
        # for page in range(1, 2):
        #     stores_data = self._fetch_page_data(page)
            
        #     if not stores_data:
        #         break

        #     for store in stores_data:
        #         #print(store)
                
        #         store_info = self._extract_store_info(store, available_value)
        #         if store_info not in save_list:
        #             save_list.append(store_info)
        #             print(f"新增店資料: {store_info}")

        #     self.add_delay()