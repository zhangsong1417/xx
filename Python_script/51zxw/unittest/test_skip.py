import unittest


class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Class module start test >>>>>>>>>>>>")

    @classmethod
    def tearDownClass(cls):
        print("Class module test end >>>>>>>>>>>>>>")

    def setUp(self):
        print("Tset1 start")

    # @unittest.skipIf(4 > 3, "skip test_c")
    def test_c(self):
        print("test_c")

    # @unittest.skipUnless(0 > 1, "skip test_b")
    def test_b(self):
        print("test_b")

    def tearDown(self):
        print("Test1 end!")


# @unittest.skip("skip Test2")
class Test2(unittest.TestCase):
    def setUp(self):
        print("Test2 start")

    def test_d(self):
        print("test_d")

    @unittest.expectedFailure
    def test_a(self):
        print("test_a")

    def tearDown(self):
        print("Test2 end!")


if __name__ == '__main__':
    unittest.main()

