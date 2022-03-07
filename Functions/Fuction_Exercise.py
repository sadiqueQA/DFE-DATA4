# # Create a new python file. In that file create a program that works out a grade based on marks with the 
# use of functions.

# The program should take the students name, homework score (/25), assessment score (/50) and final exam 
# score (/100) as inputs, and output their name and final ICT grade as a percentage.

# Reminder: any inputs and prints should not be included inside the function definition, and should strictly 
# be done outside.

# Stretch goal: Include grade boundaries such that the program also outputs a grade for the student (A, B, etc.)

def grade(homework, assessment, finalexam):
    finalscore = ((int(homework) + int(assessment) + int(finalexam)) / 175 * 100)
    if int(finalscore) >= 90:
        gradescore = "A"
    elif int(finalscore) >= 80:
        gradescore = "B"
    elif int(finalscore) >=70:
        gradescore = "C"
    else:
        gradescore = "F"
    return (gradescore, finalscore) 

name = input("What is students name? ")
homework = input('Enter ' + name + "'s" + ' homework score...')
assessment = input('Enter ' + name + "'s" + ' assessment score...')
finalexam = input('Enter ' + name + "'s" + ' final exam score...')

totalscore = grade(homework, assessment, finalexam)
print(name + " scored a grade " + totalscore[0] + " at " + str(round(totalscore[1],0)) + "%")