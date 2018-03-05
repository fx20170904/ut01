# _*_coding:utf-8__
# __authon__ = '苦叶子'
import unittest
import sys

# 被测试函数
def add(a, b):
    return a + b


class demoSkipTest(unittest.TestCase):
    @unittest.skip(u"强制跳过示例")
    def test_add(self):
        self.assertEqual(add(4, 5), 9)

    def test_add2(self):
        self.skipTest("强制跳过示例2")
        self.assertEqual(add(4, 5), 9)


if __name__ == '__main__':
    unittest.main(verbosity=2)
