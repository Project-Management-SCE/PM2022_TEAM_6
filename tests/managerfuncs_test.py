import sys
import unittest

from manager.models import School

sys.path.append('../')
from funcs.managerfuncs import get_data, addschooll


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_data()[0], "adam")
        self.assertEqual(get_data()[1], "12345")
        self.assertNotEqual(get_data()[0], "ben")
        self.assertNotEqual(get_data()[0], "56789")

    def test_something2(self):
        c = addschooll(name="kkkkk", town="test", xaxis=0, yaxis=0)
        print(c)
        cc = School.objects.get(name="kkkk")
        self.assertEqual(cc.town, "test")
        self.assertEqual(cc.x_axis, 0)
        self.assertEqual(cc.y_axis, 0)
        c.delete()


if __name__ == '__main__':
    unittest.main()
