i = 1
while i < 3:
    print(i)
    i += 1 #while 迴圈如果没有i+=1 會是無限迴圈， 開發者會需要自己控制什麼時候結束迴圈
    
# for 迴圈則不需要自己控制，它會自己結束， for 迴圈用來走訪清單中的所有元素，他是一個陣列。

#最直覺的區分方式就是：
#for 迴圈： 重視「次數」或「範圍」（我知道要跑幾次，或要把這堆東西跑完）。
#while 迴圈： 重視「狀態」或「條件」（我不知道要跑幾次，只要條件滿足就一直跑，直到條件不滿足為止）。

#所以在寫code的時候，當不知道要用哪一種迴圈， 問自己“你知不知道要跑幾次？”


# 舉例來說：
# for:你要走訪一個購物車裡的所有商品，清單裡有10件商品，這時候你會用 for
# while: 停車場的停車格，我不知道今天會有多人造訪我的停車場(不知次數)，只要“被使用的車格 < 總車格數”，我就放車進到停車塲

# #while 是判斷條件，通常不會只有一個
# total_parking_space = 100
# occupied_spaces = 0
# while occupied_spaces < total_parking_space:
#     print("allow car")
#     #occupied_spaces +=1 or occupied_spaces -= 1
    
