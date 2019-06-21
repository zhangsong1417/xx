from calculator import *
import unittest


class Test_StartEnd(unittest.TestCase):
    def setUp(self):
        print("test start")

    def tearDown(self):
        print("test end")


class Testadd(Test_StartEnd):
    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)


class Testsub(Test_StartEnd):
    def test_sub(self):
        i=Math(10,5)
        self.assertEqual(i.sub(),5)


if __name__=='__main__':
    unittest.main()