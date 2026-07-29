#methods and Function都是一樣的東西，只是在python裡面，會根據使用位置來稱呼
# Java 稱為 method, javascript 稱為 method, python 稱為 function



#宣告方法
def say_hello():
    print("Hello")

def say_hello_with_name(name): #name 是參數1
    print("Hello " + name)


#假設這是內部的商業規則
#要不要有return, 取決於這個方法的結果需不需要有後續的處理
#如果沒有return，結果不會有近一步計算

def f_to_c(f_temp):
    # Convert Fahrenheit to Celsius using the formula: C = (F - 32) * 5/9
    return (f_temp - 32) * 5 / 9 * 1.2
    
def f_to_c_v1(f_temp):
    return (f_temp - 32) * 5 / 9 * 1.1

def sum_up(num1 , num2 , num3):
    return num1*  0.1 + num2 * 0.2 + num3 * 0.3

def sum_up_list(score_list):
    total = 0
    for item in score_list:
        total += item
    return total




for i in range(3):
    say_hello_with_name(str(i))
    say_hello() #呼叫方法


print(f_to_c(80))
print(f_to_c_v1(32))
print(f_to_c(50))
print(sum_up(1,2,3))

print(sum_up_list([1,2,3,4,5]))
print(sum_up_list((0,2,3)))



result = f_to_c(80)
result += 20 # 加入自己的商業邏輯
print(result)

result_1 = f_to_c(80)
result_1 += 10
print(result_1)