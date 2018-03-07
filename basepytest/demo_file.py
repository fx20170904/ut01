# file_path = 'E:\PyWork\\ut01\\text_files\pi_digits.txt'
# with open(file_path) as file_object:
#     # contents = file_object.read()
#     # print(contents.rstrip())
#
#     # for line2 in file_object:
#     #     print(line2.rstrip())
#
#     lines = file_object.readlines()
#
# # for line in lines:
# #     print(line.rstrip())
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# print(pi_string)
# print(len(pi_string))

# file_path = 'E:\PyWork\\ut01\\text_files\py_doing.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
#     print(contents)

# file_path = 'E:\PyWork\\ut01\\text_files\py_doing.txt'
# with open(file_path) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# file_path = 'E:\PyWork\\ut01\\text_files\py_doing.txt'
# with open(file_path) as file_object:
#     lines = file_object.readlines()
#
# contents = ''
# for line in lines:
#     contents += line.replace('Python', 'C')
# print(contents)

# file_name = 'guest.txt'
# contents = input('Please input your name:')
# with open(file_name, 'a') as file_object:
#     file_object.write(contents)

file_name = 'guest_book.txt'
while True:
    contents = input("input your name:")
    with open(file_name,'a') as file_object:
        file_object.write(contents + '\n')
