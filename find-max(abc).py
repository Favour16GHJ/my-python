first_num = float(input("Enter first num: "))
second_num = float(input("Enter second num: "))
third_num = float(input("Enter third num: "))

def find_max(a,b,c):
    if a > b and a > c:
        print(f"{a} is the greatest number.")
    elif b > a and b > c:
        print(f"{b} is the greatest number.")
    elif c > a and c > b:
        print(f"{c} is the greatest number.")
    elif a == b and a > c:
        print(f"{a} and {b} are equal and the greatest numbers.")
    elif a == c and a > b:
        print(f"{a} and {c} are equal and the greatest numbers.")
    elif b == c and b > a:
        print(f"{b} and {c} are equal and the greatest numbers.")
    else:
        print("All three numbers are equal.") 

find_max(first_num, second_num, third_num)