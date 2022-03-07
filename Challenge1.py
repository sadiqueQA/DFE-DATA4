def string_fun(string):
    '''
    Return a tuple with three elements.
    The first element is True if the string contains only alphabet characters, otherwise False.
    The second element is True if the string ends with an exclamation mark ('!'), otherwise False.
    The third element is the string with all spaces (' ') replaced with hyphens ('-').
    Arguments
    string: a string
    Examples
    string_fun('Hello World!') returns (False, True, 'Hello-World!')
    string_fun('ThisIsAChallenge') returns (True, False, 'ThisIsAChallenge')
    '''

    # ====================================
    # Do not change the code before this

    # CODE1: Write code that will assign details with the appropriate tuple
    details = (True, False, '-')

    for alpha in details:
        if str.isalpha():
            print(details[0])
        else:
            print(details[1])

    for symbol in details:
        if str.endswith("!"):
            print(details[0])
        else:
            print(details[1])

    # ====================================
    # Do not change the code after this

    return details


if __name__ == '__main__':
    print(string_fun('Hello World!'))
    print(string_fun('ThisIsAChallenge'))