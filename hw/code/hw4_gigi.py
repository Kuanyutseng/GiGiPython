#這一個visitor 是包著“字典型態”的陣列
#所以 visitors 是一個陣列，沒有錯
visitors = [
    {'age':35,'express_pass':True},
    {'age':8,'express_pass':False},
    {'age':70,'express_pass':True},
    {'age':15,'express_pass':False},
    {'age':-2,'express_pass':False}
]

#如果 資料是可以要計算的，用"數字"型別，例如：身高 體重 薪水 
#如果 資料不是可以要計算的，用"文字"型別，例如：手機號碼、身分證字號、座號

# visitors = [
#     {'age':'35'},
#     {'age':'8'},
#     {'age':'70'},
#     {'age':'15'},
#     {'age':'-2'}]




total_payment=0
has_child = False
has_elder = False

for visitor in visitors:
    print("1.")
    print(visitor)
    #visitors['age']= age
    age = visitor['age']
    #visitors['express_pass'] = express_pass
    express_pass= visitor['express_pass']

    
    if age < 0:
        print('年齡輸入錯誤：'+'age')
        continue
    if age >= 12 and age < 65:
        total_payment = total_payment + 500
    elif age < 12:
        has_child = True
        total_payment = total_payment + 250
    else:
        has_elder = True
        total_payment = total_payment + 200


    if express_pass == True:
        total_payment += 150
    

print('購票總金額（折前）:'+ str(total_payment)+'元')
# has_child: False
if has_child == True and has_elder == True:
    print('符合兒童與敬老同行優惠，折抵 100 元！')
    total_payment -= 100



print(total_payment)


print('age')
print('express_pass')

#變數轉字串 要用str()
#如果只是一般字串，用雙引號包起來就行了


print('最終需支付金額：'+ str(total_payment)+'元')