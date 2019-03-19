### FUNCTION 1##

def bubble_sort(items):
    for item in range(len(items)-1, 0, -1):
        for i in range (item):
            if items [i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items


### FUNCTION 2 ###

def merge_sort(items, ascending = True):
    result = []
    if len(items) == 1:
        return items
    mid = len(items) // 2

    teilliste1 = merge_sort(items[:mid])

    teilliste2 = merge_sort(items[mid:])

    x, y = 0, 0
    while x < len(teilliste1) and y < len(teilliste2):
        if teilliste1[x] > teilliste2[y]: # < for descending
            result.append(teilliste2[y])
            y = y + 1

        else:
            result.append(teilliste1[x])
            x = x + 1


    result = result + teilliste1[x:]

    result = result + teilliste2[y:]
    if ascending == True :
        return result
    else:
        result.reverse()
        return result



### FUNCTION 3 ###

import random

def quick_sort(items):
    print('Quicksort, Parameter L:', items)
    if len(items) <= 1:
        return items
    smaller, equal, larger = [], [], []
    pivot = random.choice(items)

    for x in items:
        if x < pivot: smaller.append(x)
        elif x == pivot: equal.append(x)
        else: larger.append(x)

    print('result: ', quick_sort(smaller) + equal + quick_sort(larger))
    return quick_sort(smaller) + equal + quick_sort(larger)
