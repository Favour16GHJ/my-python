# 5. **Leap Year Checker**
#    Ask for a year and print whether it’s a leap year or not.
#    (Hint: A leap year is divisible by 4 but not 100, except if divisible by 400.)


year = int(input("Enter a year: "))

if year % 4 == 0:
    if year% 100 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year')
        else:   
            print(f'{year} is not a leap year')
    else:
            print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')


# Alternative solution:
# year = int(input("Enter a year: "))
# if year % 400 == 0:
#     print(f'{year} is a leap year')
# elif year % 100 == 0: 
#     print(f'{year} is not a leap year') 
# elif year % 4 == 0:
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not a leap year')




# elif year % 4 == 0:
#     print(f'{year} is a leap year')
# elif year % 400 == 0:
#     print(f'{year} is a leap year')
# elif year % 100
# else:
#     print(f'{year} is not a leap year')
