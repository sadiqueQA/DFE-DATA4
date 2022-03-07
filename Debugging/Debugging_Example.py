import pdb
pdb.set_trace()

def tail_recursion(factorial, result = 1): #A function to find the factorial of a number using tail recursion
    if factorial == 1:
        return result
    else:
        return tail_recursion((factorial-1),(factorial * result))

print(tail_recursion(5))
