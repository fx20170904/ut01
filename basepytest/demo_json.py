import  json
#
# # numbers = [2, 3, 5, 7, 11, 13]
#
# filename = 'number.json'
# # with open(filename, 'w') as f_obj:
# #     json.dump(numbers, f_obj)
#
# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
#
# print(numbers)

# username = input("what is your name? ")
#
# filename = 'username.json'
# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("we will remember you when you came back, " + username + "!")

# filename = "username.json"
#
# with open(filename) as f_obj:
#     username = json.load(f_obj)
#     print("Welcome back, " + username + "!")

# numbers = input("Please input your favorite number: ")
# with open('favnum.json', 'w') as f_obj:
#     json.dump(numbers, f_obj)
#
# with open('favnum.json') as ff_obj:
#     numberf = json.load(ff_obj)
#     print("I know your favorite number is " + numberf)

# filename = 'aaa.json'
# try:
#     with open(filename) as f_obj:
#         numbers = json.load(f_obj)
# except:
#     numbers = input("Please input your favorite number: ")
#     with open(filename, 'w') as f_obj:
#         json.dump(numbers, f_obj)
# else:
#     print("Your favorite number is " + numbers)


def get_stored_number():
    """获取存储的数字"""
    filename = 'ddd.json'
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except:
        return None
    else:
        return number

def get_new_number():
    """存储数字"""
    filename = 'ddd.json'
    number = input("Please input your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(number,f_obj)
    return number

def yfn():
    """输出最爱数字"""
    number = get_stored_number()

    if number:
        print("你最喜欢的数字是 " + number + "吗？ 是——Y,否——N")
        while True:
            result = input("your answer is: ")
            if result == 'Y':
                print("OK, NOW I know your favorite number is " + number + '.')
                break
            elif result == 'N':
                get_new_number()
                break
            else:
                print("the input is invalid")

        # if result == 'Y':
        #     print("OK, NOW I know your favorite number is " + number + '.')
        # elif result == 'N':
        #     get_new_number()
        # else:
        #     print("the input is invalid")
    else:
        number = get_new_number()
        print("First input, your favorite number is " + number + '.')

yfn()



