# universal = {1, 'cat', 'apple', True}
# print(universal)
# for i in universal:
#     print(i)

set1 = {"apple","banana", "cherry", "mango"}
set2 = {"pinapple","mango","papaya"}

universal = set1.symmetric_difference(set2)
print(universal)

cardict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
for i in cardict.items():
    print(i)
# print(cardict)
