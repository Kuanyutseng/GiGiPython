# x = age
# family_age=[35,8,70,15,-2, 35]
# if x >=12 and x < 65:
#     adult_price = str(500) + '元'
# elif x < 12 :
#     child_price = str(250) + '元'
# else :
#     elder_price = str(200) + '元'
# for 快速通關 in family_age:
#     if x>=0:
#         print('年齡輸入錯誤：'+ str(x))
#     continue
#     if x == 35 and x == 70:
#         price+=150
#     else:
#         price=price
# print('購票總金額：'+ str(price))
  
  #{"age": 8, "expressPass": False},
# input
visitors = [{"age": 35, "expressPass": True},
          
            {"age": 70, "expressPass": True},
            {"age": 15, "expressPass": False},
            {"age": -2, "expressPass": False}]



total_price = 0
have_under_12 = False
have_over_65 = False


for visitor in visitors:
    price_per_person = 0
   
    age = visitor["age"]
    have_express_pass = visitor["expressPass"]
    

    if age < 0:
        print("年齡輸入錯誤:", age)
        continue

    
   

    if age >= 12 and age < 65:
        price_per_person += 500
    elif age < 12:
        price_per_person += 250
    else:
        price_per_person += 200

    if have_express_pass:
        price_per_person += 150
    
    if age < 12:
        have_under_12 = True
    elif age >= 65:
        have_over_65 = True

    total_price += price_per_person

print("購票總金額（折前）：", total_price)
print("=" * 30)

if have_under_12 and have_over_65:
    total_price -= 100
    print("符合兒童與敬老同行優惠，折抵 100 元！")

print("最終需支付金額：", total_price)








