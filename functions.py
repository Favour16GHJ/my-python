
# # def myfunction():
# #     print("Welcome to my new function")
# # myfunction()

# # add  = lambda x, y: x + y
# # result = add(5, 3)

# # def doubler(n):
# #     return lambda a: a * n
# # x = doubler(5)
# # print(x(2))

# # Arbitrary arguements
# def myfunction(*kids):
#     print(kids)

# myfunction("Emil", "Tobias", "Linus")

# # Keyword Arguements
# def my_function(**kids):
#     print(kids)
#     # print(f"His last name is {kids{'lname'}}")

# my_function(fname = "Tobias", lname = "Refsnes")

def countdown(n):
    if n <= 0 :
        print("Done")
    else:
        print(n)
        countdown(n-1)
# countdown()



def factorial(n):
    if n == 0 or n == 1:
        return 1 
    else:
        return n * factorial(n-1)
print(factorial(5))