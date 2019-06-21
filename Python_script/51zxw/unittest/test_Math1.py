from calculator import Math
import unittest


class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start")

    # def test_add(self):
    #     j = Math(5, 10)
    #     self.assertEqual(j.add(), 15)
    #     # 用例失败场景
    #     self.assertEqual(j.add(), 12)
    #
    # def test_add1(self):
    #     j = Math(5, 10)
    #     self.assertNotEqual(j.add(), 12)

    # def test_assertTrue(self):
    #     j = Math(5, 10)
    #     self.assertTrue(j.add() > 10)
    #
    # def test_assertIs(self):
    #     self.assertIs("vorx", 'vorx')
    #     self.assertIs("vorx", "123")

    # def test_assertIn(self):
    #     self.assertIn("vorx", "hello,vorx")
    #     self.assertIn("123", "hello,vorx")
    # def test_assertIsNot(self):
    #     self.assertIsNot("vorx", "123")
    #     self.assertIsNot("vorx", "vorx")

    def test_assertNotIn(self):
        self.assertNotIn("vorx", "hello,vorx")
        self.assertNotIn("123", "hello,vorx")

    def tearDown(self):
        print("test end")


if __name__ == '__main__':

    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestMath("test_assertNotIn"))
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)
