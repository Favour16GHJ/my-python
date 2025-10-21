# Write a program that uses a while loop to display the multiplication table of a particular integer(user defined)

value = int(input("Enter a value: "))

i = 1
while i <= 12:
    print(f" {value} x {i} = {value*i} ")
    i += 1