### FUNCTION 1 ###

def sum_array(array):
    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])



### FUNCTION 2 ###

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)



### FUNCTION 3 ###

def factorial(n):
    return 1 if (n < 1) else n * factorial(n-1)



### FUNCTION 4 ###

def reverse(word):
    if word == "":
        return word
    else:
        return word[-1] + reverse(word[:-1])
