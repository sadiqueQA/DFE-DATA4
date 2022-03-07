# Create a new Python file and write a program that does the following:

# Asks for an input from the user as a mark.
# - If the mark is greater that 85 print "Distinction"
# - If the mark is between 65 and 85 print "Pass"
# - Anything else print "Fail"
# Try to do this both with and without elif statements.

mark = int(input("Enter mark: "))

if mark > 85:
    print("Distinction")
elif mark >= 65 and mark <= 85:
    print("Pass")
else:
    print("Fail")