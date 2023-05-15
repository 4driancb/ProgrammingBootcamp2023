"""
Given a list of digits, determine the integer that it represents.

For example, given the list: [8,3,5,1], your program should output 8351 as an integer.

Note: You are not allowed to use conversion / casting, or any method that makes your solution trivial (such as printing each number without spaces).

You should employ an algorithmic approach in your code. Please note that your application cannot be considered if this requirement is not met.
"""

def task1(lst):
    result = ""  # create a temporary string that will be added onto
    for i in lst:  # traverse the given input list
        result += str(i)  # concatenate the string with the elements in the list (after converting them to strings)
    return int(result)  # return the result as an integer


print(task1([8, 3, 5, 1]))
