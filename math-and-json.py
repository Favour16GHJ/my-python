# import math
# x = math.pi
# print(x)

# import json
# # print(dir(json))
# x = '{"name" : "john", "age" : 30, "city" : "new york" }'
# print(type(x))
# y = json.loads(x)
# print(type(y))
# d = json.dumps(y)

# Formatting json
import json
x = {"name":"John", "age":30, "married":True, "divorced":False,"children": ["Ann", "Billy"], "pets":["dogs", "cats"], "cars" : []}
# print(json.dumps(x))
print(json.dumps(x, indent = 4))
# print(json.dumps(x, indent = 4, sort_keys = True))
