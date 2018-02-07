def if_demo(a):
    """
    if语句示例
    :param a: 
    :return: 
    """
    if a < 1 :
        print('a<1')
    elif a < 2 :
        print('1<=a<2')
    else:
        print('a>=2')
import requests
import time
def while_demo():
    sums = 5
    """
    while演示
    :return: 
    """
    while sums > 0:
        res = requests.get('http://www.baidu.com')
        print(res.status_code)
        sums -=1
def for_demo():
    """
    for语句演示
    :return: 
    """
    name_list = ['Cathy','Terry','Joe','Heather']

    print('序列项迭代')
    for eachName in name_list:
        print(eachName)

    print('序列索引迭代')
    for index in range(0,len(name_list)):
        print(name_list[index])

def exception_demo():
    """
    异常捕捉展示
    :return: 
    """
    while True:
        try:
            print('run in try')
            a = 1
            print(a)
            b = a/0
            print(b)
            c = 2
            print(c)
        except BaseException as e:
            print(e)
        finally:
            print('finally')
        time.sleep(2)
def fun_demo_0():
    """
    返回0个对象
    :return: 
    """
    print('return 0 object')
def fun_demo_1():
    """
    返回1个对象
    :return: 
    """
    print('return 1 object')
    return 1
def fun_demo_more():
    """
    返回多个对象
    :return: 
    """
    print('return more objects')
    return 1, 2, 3
def function_demo():
    """
    函数返回演示
    :return: 
    """
    print(fun_demo_0())
    print(fun_demo_1())
    print(fun_demo_more())


if __name__ == '__main__':
    #if_demo(1)
    #while_demo()
    #for_demo()
    #exception_demo()
    function_demo()