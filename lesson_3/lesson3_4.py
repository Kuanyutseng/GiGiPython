# dictionary 字典
# key(文字) : value(可以是文字，數字，陣列，字典....)
# 用大括號{}括起來

age = 25

gigi = {
    "name": "gigi",
    "age": 26,
    "gender": "female",
    "hobbies": ["golf", "sleep"],
    "fridge": {
        "apple": 3,
        "orange": 4,
    }
}


print(gigi)
print(gigi["name"])
print(gigi["hobbies"])
print(gigi["fridge"]["apple"])

# 我把gigi這個變數裡name的值，儲存在name這個變數裡
name = gigi["name"]

# 我把gigi這個變數裡lastName的值，變成lee
gigi["lastName"] = "lee"
print(gigi)

del gigi["age"]
print(gigi)
