# Assignment 8

"""

Return the sum of the numbers in the list, except ignore sections of
numbers starting with a 7 and extending to the next 8
(every 7 will be followed by at least one 8).
Return 0 for no numbers.

EXAMPLE:
sum78([1, 2, 2]) → 5
sum78([1, 2, 2, 7, 99, 99, 8]) → 5
sum78([1, 1, 7, 8, 2]) → 4

"""

#Your Code Below:
def sum78(list_num):
    sum_of_list = 0
    in_range = False
    for i in range(len(list_num)):
        if list_num[i] == 7:
            in_range = True

        if in_range ==False:
            sum_of_list += list_num[i]

        if list_num[i] == 8:
            in_range = False

        # if list_num[i] != 7:
        #     sum_of_list += list_num[i]
        # elif list_num[i] == 7:
        #     for j in range(i,len(list_num)):
        #         if(list_num[i] == 8):
        #             break
    return sum_of_list

print(sum78([1, 2, 2]))















print(sum78([1, 2, 2])) #→ 5
print(sum78([1, 2, 2, 7, 99, 99, 8])) #→ 5
print(sum78([1, 1, 7, 8, 2])) #→ 4



























# Solution:

# def sum78(nums):
#     sum = 0
#     inRange = False
#
#     for i in range(len(nums)):
#         if nums[i] == 7:
#             inRange = True
#
#         if not inRange:
#             sum += nums[i]
#
#         if inRange and nums[i] == 8:
#             inRange = False
#
#     return sum