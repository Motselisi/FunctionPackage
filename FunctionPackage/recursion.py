def sum_array(array):
    return(sum(array))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n <1:
        return 1
    else:
        returnNumber = n * factorial( n - 1 )
    print(str(n) + '! = ' + str(returnNumber))
    return returnNumber

def reverse(word):
    if word == "":
        return word
    else:
        return word[-1] + reverse(word[:-1])
