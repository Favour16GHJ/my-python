# Write a program to convert a student's score into a grade.
# A = 80 -100
# B = 70 - 79
# C = 60 - 69
# D = 50 - 59
# E = 40 - 49
# F = 0 - 39

score = int(input("Enter score (0-100): "))

if score >= 80 and score <= 100:
    print(f"{score} is an A")
elif score >= 70 and score < 80:
    print(f"{score} is a B")
elif score >= 60 and score < 70:
    print(f"{score} is a C")    
elif score >= 50 and score < 60:
    print(f"{score} is a D")
elif score >= 40 and score < 50:
    print(f"{score} is an E")
elif score >= 0 and score < 40:
    print(f"{score} is an F")
else:
    print(f"{score} is an invalid score")