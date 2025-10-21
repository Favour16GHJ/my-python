# Write a program to calculate the Body Mass Index (BMI) and categorize it. NB BMI is calculated as weight (kg) / (height (m))^2.
# BMI Categories: 

# Underweight: BMI less than 18.5
# Normal weight:  BMI between 18.5 and 24.9 
# Overweight:  BMI between 25 and 29.9
# Obesity: BMI higher than 30  
  

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
# bmi_1dp = f"{bmi:.1f}"
# print(f"Your BMI is {bmi:.1f}")

if bmi >= 30.0:
    print(f"Person is Obese with BMI of {bmi:.1f}")
elif bmi < 30.0 and bmi >= 25.0:
    print("Person is Overweight with BMI of {bmi:.1f}")
elif bmi < 25.0 and bmi  >= 18.5:
    print("Person is of Healthy Weight with BMI of {bmi:.1f}")
elif bmi < 18.5:
    print("Person is Underweight with BMI of {bmi:.1f}")
else:
    print("Recheck Algorithm with BMI of {bmi:.1f}")

# num = float(input("num: "))
# num_2dp = f"{num:.1f}"
# print(num_2dp)
# print(f"{num:.1f}")
# output : 
# num: 34.567
# 34.6