# x = int(input("enter a value: "))
# for i in range(1, x+1 ):
#     print("*" * i)


# a = int(input("enter a value: "))
# for i in range(1, i+1):
#     a *= 1

# print(a) 

# num = input("enter word: ")
# vowels = 'aeiou'
# count = 0
# for i in num:
#     # print(i)
#     if i in vowels:
#         count = count + 1
# print(count)


# word = input("enter a word: ")
# reverse_word = word[::-1]
# if word == reverse_word:
#     print("palindrome") 
# else:
#     print("not a palindrome")

# a = "hello"
# print(a[::-1])
# b = a.split()
# print(a.upper())
# print(a).reverse()
# print(b).reverse()
# c = ''.join(b)
# print(a[-4:-1])

# Operations
# yob = int(input("enter your year of birth: "))
# print(f"Hi, I am {2025-yob} years old")

# #Modifiers
# price = 59
# print(f"The price is {price:.2f} dollars")

# txt = "We are the so-called \"Vikings\" from the north."
# txt = "We are the so-called Vikings from \rthe north."
# txt = "We are the so-called Vikings from \tthe north."
# txt = "We are the so-called Vikings from \bthe north."
# print(txt)



list_1 = list((["apple"], "banana", True, "apple", 12, 12.6, ()))
# print(list_1[-5:-2])
# list_1[1:2] = ["kiwi", "pineapple", "grapes"]
# list_1[1:3] = ["kiwi"]
# list_1.insert(1, "watermelon")
# print(list_1)

# list_1.append("orange")
# list_2 = ("a", "b", "c")
# list_1.extend(list_2)
# print(list_1)

# del list_1[5]
# list_1.clear()
# del list_1
# print(list_1)



tuple_1 = tuple((["apple"], "banana", True, "apple", 12,"apple", 12, 12.6, ()))
print(tuple_1.count(12))
print(tuple_1.index(12))