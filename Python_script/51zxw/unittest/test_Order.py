import unittest


class Test1(unittest.TestCase):
    def setUp(self):
        print("Tset1 start")

    def test_c(self):
        print("test_c")

    def test_b(self):
        print("test_b")

    def tearDown(self):
        print("Test1 end!")


class Test2(unittest.TestCase):
    def setUp(self):
        print("Test2 start")

    def test_d(self):
        print("test_d")

    def test_a(self):
        print("test_a")

    def tearDown(self):
        print("Test2 end!")


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Test2("test_d"))
    suite.addTest(Test1("test_b"))
    suite.addTest(Test2('test_a'))
    suite.addTest(Test1('test_c'))

    runner = unittest.TextTestRunner()
    runner.run(suite)

