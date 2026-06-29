cart = ["apple", "banana", "milk", "bread", "egg"]
is_vip = True
wallet_balance = 350
total_price = 500
if 'milk' in cart:
    if is_vip == True and len(cart) >= 5:
        total_price -= 200
        print(total_price)
    else:
        total_price -= 50
        print(total_price)
else:
    if is_vip == True:
        wallet_balance -= 100
        print(wallet_balance)
    
    else:
        print(wallet_balance)

if wallet_balance >= total_price:
    wallet_balance -= total_price
    print('購買成功！剩餘餘額'+ ':' + str(wallet_balance))
else:
    print('餘額不足')
    cart.remove('egg' and 'bread')
    print('已移除部分商品，目前購物車清單: '+ str(cart))