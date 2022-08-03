# Assignment 1:

import sys
import os
import re

# directory_containing_files = "/Users/imtiazahmad/PycharmProjects/Assignments/Section_06/project_files" #sys.argv[1]
# words_to_aggregate = ["hello", "Peter", "computer"] #sys.argv[2:]
# os.chdir("project_files")
# print(os.getcwd())
directory_containing_files = "C:/Users/faroo/Desktop/Python Certification Course/PythonCourse-master/Section_06/project_files"
words_to_aggregate = ["there", "Michael", "running"]

# Expected Output:
# {"there": n, "Michael": n, "running": n}

# Your Code Below:

words_and_counts = {}

for word in words_to_aggregate:
    count = 0
    for path, folder_names, file_names in os.walk(directory_containing_files):
        for file_name in file_names:
            file = os.path.join(path, file_name)
            with open(file, "r") as a_file:
                for line in a_file:
                    if re.search(word, line):
                        word_list = re.findall(word, line)
                        count += len(word_list)

    words_and_counts[word] = count

print(words_and_counts)

# Solution:
# words_and_counts = {}
#
# for word in words_to_aggregate:
#     count = 0
#     for path, folder_names, file_names in os.walk(directory_containing_files):
#         for file_name in file_names:
#             file = os.path.join(path, file_name)
#             with open(file, "r") as a_file:
#                 for line in a_file:
#                     if re.search(word, line):
#                         word_list = re.findall(word, line)
#                         count += len(word_list)
#
#     words_and_counts[word] = count
#
#
#
# print(words_and_counts)
