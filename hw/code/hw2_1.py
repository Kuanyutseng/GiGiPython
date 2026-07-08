base_price = 485
has_coupon = True
vip_level = "Gold"
payment_method = "Cash"
base_rate = 0.1

if payment_method == 'Card':
    service_charge = base_price * (base_rate + 0.02)
    print(int(service_charge))
else:
    service_charge = base_price * base_rate
    if has_coupon and vip_level == "Gold" and base_price >= 400:
        final_price = base_price - 80
        service_charge = 0
    elif has_coupon and (vip_level == "Gold" or base_price <= 400):
        final_price = base_price - 50
        service_charge = base_price *base_rate
    elif has_coupon and vip_level == "Gold":
        final_price = base_price - 20
        service_charge = base_price *base_rate
    else:
        final_price = base_price
if final_price % 2 == 0:
    print("最終結帳金額為偶數，獲得 5 點點數！")
else:
    print("最終結帳金額為奇數，獲得 10 點點數！")
print('最終結帳金額為:'+ str(final_price) + '元')