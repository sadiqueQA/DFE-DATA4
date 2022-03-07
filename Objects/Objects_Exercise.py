# In a new Python file, create a class of students.

# It should contain the following attributes: name, age, and class with default value "student".

# It should also contain a method which takes in 3 test scores and prints the students average test score.


class student:

    def __init__(self, name, age, averagescore):
        self.name = name
        self.age = age
        averagescore
    
    def averagescore(self, test1, test2, test3):
        average = sum((test1 + test2 + test3)/3)
        return average


John = student("John", "21", averagescore(50, 60, 80)) 


Jane = student("Jane", "22")
(35, 77, 90)

Jack = student("Jack", "23")
(19, 30, 88)

print(getattr(John, "name") + " is " + getattr(John, "age") + " and scored an average of " + getattr(John, averagescore))
