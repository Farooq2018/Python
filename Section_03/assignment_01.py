# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""


# your code below:
def merge_lists(list1, list2):
    result = list1 + list2
    return result


list1 = [1, 2, 3, 4, 5, 6]

list2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(merge_lists(list1, list2))

# solution Below:

# def merge_lists(list_a, list_b):
#     return list_a + list_b
#
# my_list = merge_lists([1,2,3],['a', 'b', 'c'])
# print(my_list)
