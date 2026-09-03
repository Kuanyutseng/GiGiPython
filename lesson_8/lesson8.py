# 引入json library
import json
# object to json
array = ["apple", "banana", "cherry", 'hello world']
print(array) #

json_string = json.dumps(array)
print(json_string)


# json to object
json_array = json.loads(json_string)
print(json_array)


gigi = {
    "age": 25,
    "name": "gigi",
    "student": True,
    "grades": [99, 88, 77],
    "address":{
        "city": "taipei",
        "distric": "daan"
    }
}
print(gigi)

#將object 存到json
gigi_json = json.dumps(gigi)
print(gigi_json)








