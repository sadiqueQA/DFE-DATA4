myfile = open('README.md')
chars = myfile.readlines()
chars.insert(2,"I like files\n")
chars.append("Cheese is pretty good to eat\n")
print(chars)

for i in chars:
    output = output + i

myfile = open('README.md', mode='w')
