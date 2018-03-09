import unittest
from city_functions import city_function

class TestCityFunction(unittest.TestCase):
    """测试城市函数返回值"""

    def test_city_country(self):
        """正常返回功能"""
        ccstr = city_function('天津', '中国')
        self.assertEqual(ccstr, '天津,中国')

    def test_city_country_population(self):
        """正常返回加人口"""
        ccstr = city_function('天津', '中国', 1000)
        self.assertEqual(ccstr, '天津,中国 1000')
unittest.main()