from calculator import Math
import unittest


class Test_add(unittest.TestCase):
    def setUp(self):
        print("Test_add start")

    def test_add(self):
        j = Math(5, 10)
        self.assertEqual(j.add(), 15)

    def test_add1(self):
        j = Math(5, 10)
        self.assertNotEqual(j.add(), 15)

    def tearDown(self):
        print("Test_add end")


class Test_sub(unittest.TestCase):
    def setUp(self):
        print("Test_sub start")

    def test_sub(self):
        i = Math(5, 10)
        self.assertEqual(i.sub(), -5)

    def test_sub1(self):
        i = Math(5, 10)
        self.assertNotEqual(i.sub(), -5)

    def tearDown(self):
        print("Test_sub end")


if __name__ == '__main__':

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(Test_add("test_add"))
    suite.addTest(Test_add("test_add1"))
    suite.addTest(Test_sub("test_sub"))
    suite.addTest(Test_sub("test_sub1"))


    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
