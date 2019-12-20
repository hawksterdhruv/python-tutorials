# List Comprehension
# b = range(20)
# a=[]
# for x in b:
#    if x%2==0:
#        a.append(x)
# print(a)

# OR
# b = list(for x in range(20) if x % 2 == 0)
# print(b)

# filtered_list=[]
# letters = ['a','b','c','d','e','f','g','h','i','j','a','b']
# for letter in letters:
#     if letter not in ('a','b'):
#         filtered_list.append(letter)
# print(filtered_list)

# OR

# letters = ['a','b','c','d','e','f','g','h','i','j','a','b']
# list1 = [letter for letter in letters if (letter != 'a' and letter != 'b')]
# print(list1)


# x = [x **2 for x in range(20)]
# print(x)

# Celsius = [39.2, 36.5, 37.3, 37.8, 99.0, 112.0, 167]
# Fahrenheit = [((float(9)/5)*x + 32) for x in Celsius]
# print(Fahrenheit)


# list = [x*y for x in range(1,20) for y in range(2,15)]
# print(len(list))

# Generator Comprehension
# 1. """Generator comprehensions are simply like a list comprehension but with parentheses
# - round brackets - instead of (square) brackets around it"""
#
# 2. """the syntax and the way of working is like list comprehension, but a generator
# comprehension returns a generator instead of a list."""

# x = (x **2 for x in range(20))
# print(x)

# x = (x **2 for x in range(20))
# print(list(x))

# b = (x for x in range(20) if x % 2 == 0)
# print(list(b))

# Set Comprehension
# """A set comprehension is similar to a list comprehension, but returns a set and not a list"""

# b = {x for x in range(20) if x % 2 == 0}
# # print(b)

# set_of_multiply_of_list = {x*y for x in range(1,20) for y in range(2,15)}
# print(set_of_multiply_of_list)




