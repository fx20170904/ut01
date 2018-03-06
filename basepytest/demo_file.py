file_path = 'E:\PyWork\\ut01\\text_files\pi_digits.txt'
with open(file_path) as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())

    # for line2 in file_object:
    #     print(line2.rstrip())

    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())
pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

