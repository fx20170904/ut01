import time
def exception_demo():

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
            print('run in except')
            print(e)
        finally:
            print('finally')
        sleep(0.5)


exception_demo()