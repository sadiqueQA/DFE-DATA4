# QA While Loop Exercise
# Write a while loop which asks for the names of 5 people, and for each person prints their name followed by the text "is awesome!"

count = 0
while count < 5:
    name = str(input("What is your name?"))
    print(name, "is awesome")
    count +=1

# or

count = 0
friends = []

while count < 5:
    name = input("enter your name: ")
    friends.append(name)
    count +=1

for friend in friends:
    print(friend, "is awesome")