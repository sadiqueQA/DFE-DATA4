# Goal: “Create a Budget class that can instantiate objects based on different budget categories 
# - Create Class what will make a few objects
# - cat1 = class()
# - cat2 = class() 
# like food, clothing, and entertainment.


# These objects should allow for depositing and withdrawing funds from each category, 
# Action, Therefore I need to write methods
# def deposit()

# as well computing category balances and 
#  - CLasses are not just code, they are also data! Therefore a blance variable.
#  - all transactions must use the balance var

# transferring balance amounts between categories”
# - what info do I need?
#   - from cat name - this is the object we created
#   - to cat name - this is the depositi method in another class object
#   - balance amount






class Budget:

    balance = 0

    def deposit(self,moneyin):
        pass

    def withdraw(self,moneyout):
        pass

food = Budget()

food.deposit()
food.withdraw(1.99)

clothes = Budget()
house = Budget()