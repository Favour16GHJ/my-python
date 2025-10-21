# Write a program to convert a student's score into a grade.
# A = 80 -100
# B = 70 - 79
# C = 60 - 69
# D = 50 - 59
# E = 40 - 49
# F = 0 - 39

score = int(input("Enter score (0-100): "))

if score >= 80 and score <= 100:
    print(f"Your score is {score}, You got an A.")
elif score >= 70 :
    print(f"Your score is {score}, You got a B.")
elif score >= 60 :
    print(f"Your score is {score}, You got a C.")    
elif score >= 50 :
    print(f"Your score is {score}, You got a D.")
elif score >= 0 :
    print(f"Your score is {score}, You got an F.")
else:
    print(f"{score} is an invalid score")