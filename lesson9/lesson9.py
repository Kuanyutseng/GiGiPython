num1 = 1
num2 = 0
num3 = "3"
try:
    print(num1 / num2)
    print(num3 / num2)
except ZeroDivisionError as e:
    print("this is my ZeroDivisionError: " + str(e))
except TypeError as e:
    print("this is my TypeError: " + str(e))    
except Exception as e:
    print("this is my error: " + str(e))
finally:
    print("done try")    
print("done")



