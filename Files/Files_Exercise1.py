# Opens a new text file called "teams.txt" and adds the names of 5 sports teams.

file = open("teams.txt", "w")

teamlist = ["Arsenal", "Liverpool", "Chelsea", "Man City", "Man Utd"]
newline = ''

for i in teamlist:
    newline = newline + i + '\n'
file.write(newline)

file.close()

# Reads and displays the names of the 1st and 4th team in the file.

file = open("teams.txt", "r")

line = file.readlines()
print(line[0])
print(line[3])


file.close()