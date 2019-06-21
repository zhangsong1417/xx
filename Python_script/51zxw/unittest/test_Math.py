from calculator import Math
import unittest


class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    def test_add(self):
        j = Math(5, 10)
        # self.assertEqual(j.add(), 15)
        # 用例失败场景
        self.assertEqual(j.add(), 12)

    def tearDown(self):
        print("test end")


if __name__ == '__main__':

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestMath("test_add"))

    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
