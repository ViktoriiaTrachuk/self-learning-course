'''Implement the following methods:
bubble_sort - should take a list of numbers as an argument and return the new list with elements sorted in ascending order.
Also should take an optional boolean argument to change the sorting order from ascending to descending.
If a list contains non-numeric value, method should raise ValueError
'''


numbers_list = [11, 33, 90, 120, 43, 22]

#this will sort the list ascending by default:
def ascend(numbers_list):
    print(numbers_list.sort())
#to sort the list descending:
def descend(numbers_list):
    return(numbers_list.sort(reverse=True))

def type(numbers_list):
    if all(type(item) is not int for item in numbers_list):
        return ValueError
    #or
    #if any(not isinstance(num, (int, float)) for num in numbers_list):
    #    raise ValueError("Non-numeric value")

def maximum(numbers_list):
    return(numbers_list.sort[-1])

def min(numbers_list):
    return(numbers_list.sort[0])
    
def empty_list(numbers_list):
    if len(numbers_list) == 0:
        raise ValueError("The list is empty")
    #if not numbers_list:
    #raise ValueError("The list is empty")
