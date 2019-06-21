from calculator import *
from StartEnd import *


class Test_sub(Setup_tearDown):
    def test_sub(self):
        j = Math(5, 5)
        self.assertEqual(j.sub(), 10)

    def test_sub1(self):
        j = Math(8, 8)
        self.assertEqual(j.sub(), 16)
