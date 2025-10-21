# Write a program that checks the temperature of a place.
# If the temperature is 80 degrees or higher, print "It is hot."
# If the temperature is between 40 and 79 degrees, print "It is warm."
# If the temperature is below 40 degrees, print "It is cold."


temp = int(input("Enter the current temperature: "))
if temp >= 80:
    print("It is hot.")
elif (temp >= 40 and temp < 80):
    print("It is warm.")
else:
    print("It is cold.")