# coding:utf-8
import requests

__author__ = 'lfz'


def get_demo():
    """
    requests
    :return: 
    """

    url = 'http://www.baidu.com/s'
    qdata = {'wd': '神州专车'}
    res = requests.get(url,params=qdata)
    print(res.url)
    print(res.status_code)
    print(res.text)



if __name__ == '__main__':
    get_demo()
