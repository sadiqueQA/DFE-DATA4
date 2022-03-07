# Edits your "teams.txt" file so that the top line is replaced with "This is a new line".

file = open("teams.txt", "r+")

line = file.readlines
line[0]

file.write("This is the new line.\n")

# Print out the edited file line by line.



file.close()



