# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")


# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_num = input("\nFirst number: ")
#     if first_num == 'q':
#         break
#     second_num = input("Second number: ")
#     if second_num == 'q':
#         break
#     try:
#         answer = int(first_num)/int(second_num)
#     except ZeroDivisionError:
#         print("You can't divide by zero")
#     else:
#         print(answer)


# while True:
#     number = input("input the first number: ")
#     number2 = input("input the second number: ")
#     try:
#         thesum = int(number) + int(number2)
#     except ValueError:
#         print("please input number, not string")
#     else:
#         print(thesum)

# filenames = ['cats.', 'dogs.txt']
#
# for filename in filenames:
#     try:
#         with open(filename) as file_object:
#             contents = file_object.read()
#     except FileNotFoundError:
#         # print(filename + "file not found")
#         pass
#     else:
#         print(contents)

