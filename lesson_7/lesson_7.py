

#Class（類別）： 汽車工廠裡的生產模具與規格書。它定義了這款車必須有四個輪子、一個方向盤、還有引擎。

#Object（物件）： 實際從產線開出來的那台賓士或 Toyota。這台具體的車子會有自己的車牌號碼（屬性），你也可以實際踩油門讓它前進（方法）。

#這是類別
class Car:
    # __init__  是建立物件“必須”要提供的基本資料
    def __init__(self , color , brand , model , year):
        self.color = color
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    #self 的用來存取自己規格書本身的資料
    def get_color(self):
        return self.color

    def get_brand(self):
        return self.brand
    
    def get_model(self):
        return self.model

    def get_year(self):
        return self.year
    
    def set_mileage(self, mileage):
        self.mileage = mileage
    
    def get_mileage(self):
        return self.mileage

    def drive_in_sport_mode(self):
        print("driving in sport mode")

    def drive_in_normal_mode(self):
        print("drving in normal mode")
    
    def sound_horn(self, times):
        for i in range(times):
            print("ba")

    


# 這是物件
my_car = Car("blue", "toyata", "RAV4", 2025)
print(my_car.get_year())
my_car.set_mileage(99)
print(my_car.get_mileage())


my_car.drive_in_sport_mode()
my_car.sound_horn(3)
my_car.drive_in_normal_mode()

# set_mileage 是 打數值設定回去 (mileage 是物件本身的屬性)

my_car.set_mileage(my_car.get_mileage() + 10)
print(my_car.get_mileage())

# 下面這一行不成立，因為我的規格書沒有定義
#my_car.set_sound("bark")