# dictionary 字典
# key(文字) : value(可以是文字，數字，陣列，字典....)
# 用大括號{}括起來

age = 25

gigi = {
    "name": "gigi",
    "age": 26,
    "gender": "female",
    "hobbies": ["golf", "sleep"]
}


print(gigi)
print(gigi["name"])
print(gigi["hobbies"])

gigi["lastName"] = "lee"
print(gigi)

del gigi["age"]
print(gigi)
