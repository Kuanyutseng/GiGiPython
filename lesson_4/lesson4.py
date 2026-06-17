
num1 = 1
num2 = 2
num3 = 3
if num1 > num2 :
    print("num1比num2大")
elif num1 == num2:
    print("num1跟num2一樣大")
else:
    print("num2比num1大")


print("=" * 30)
if num2 > num1 :
    print("num2比num1大")
elif num3 > num2:
    print("num3比num2大")
else:
    print("else")

print("done")

print("=" * 30)
if num2 > num1:
    print("num2比num1大")


score = 92

# nested if => if 裡面還有if (他可以包無限次，但是包太多會很亂)
if score >= 90:
    if score >= 95:
        print("A+")
    else: #line 34
        add_point3 = "add_point3"
        
        if score >= 93:
            print("A")
            add_point1 = "add_point1"
        else:
            print("A-")
            add_point2 = "add_point2"
            print(add_point2)
            print(add_point3)

        print("inside of 90 and not 95") # 這裡屬於line 34
    print("happy")

elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
print("done1")
    



transcation_threshold = 100
price = 85
if transcation_threshold >= 100:
    if price > 90:
        print("sell")
    elif price < 80:
        print("buy")
