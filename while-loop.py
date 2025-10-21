# i = 1
# while i < 6:
#     print(i)
#     i += 1
# print("Loop 1 ends here.")

# a = 5
# while a > 0:
#     print(a)
#     a -= 1
# print("Loop 2 ends here.")

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         print("We are at the middle")
#     i += 1


# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         print("We are at the middle")
#         break

#     i += 1


i = 1
while i < 6:
    i += 1
    if i == 3:
        print("We are at the middle")
        continue
    print(i)
else:
    print("It is finished.")