inventory = {'apple': {'price': 30, 'stock': 5},
             'banana': {'price': 15, 'stock': 0},
             'orange': {'price': 25, 'stock': 3},
             'peach': {'price': 60, 'stock': 2}}
shopping_cart = ['apple','watermelon','banana','orange','peach']
is_vip = True
total_price = 0
for item in shopping_cart:
    if item not in inventory:
        print(item + '超市沒有販售‘!')
        continue
    else:
        stock = inventory[item]['stock']

        if inventory[item]['stock'] == 0:
            print(item + '已經售完'+','+'下次請早'+'!')
        elif inventory[item]['stock'] >= 0:
            price = inventory[item]['price']
            if price >= 50 and is_vip:
                price = int(price*0.9)
            total_price+=price
            stock-=1
            
            print('成功購買',item,'！單價：',price,'元')
print('本次購物總金額：'+str(total_price)+'元')
print(inventory)

print("====================")

inventory = {'apple': {'price': 30, 'stock': 5},
             'banana': {'price': 15, 'stock': 0},
             'orange': {'price': 25, 'stock': 3},
             'peach': {'price': 60, 'stock': 2}}
shopping_cart = ['apple','watermelon','banana','orange','peach']
is_vip = True
total_payment = 0
for item in shopping_cart:
    if item not in inventory:
        print(item + '超市沒有販售‘!')
        continue
    if inventory[item]['stock'] == 0:
        print(item + '已經售完'+','+'下次請早'+'!')
    else:
        price = inventory[item]['price']
        if price >= 50 and is_vip:
            price = int(price*0.9)
        total_payment+=price
        #inventory[item]['stock']-=1
        inventory[item]['stock'] = inventory[item]['stock'] - 1
        print('成功購買',item,'！單價：',price,'元')
print('本次購物總金額：'+ str(total_payment)+'元')