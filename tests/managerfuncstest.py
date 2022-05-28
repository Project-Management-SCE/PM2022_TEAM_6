import sys
import unittest
from django.test import TestCase

from manager.models import School, messegerequest
from voulnteers.models import volnteer

sys.path.append('../')
from funcs.managerfuncs import get_data, addschooll, addmessegerequest, getemptyschools, getfullschools, addcoordinator, \
    getcoordinators, getaboutus, changeaboutus

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_data()[0], "adam")
        self.assertEqual(get_data()[1], "12345")
        self.assertNotEqual(get_data()[0], "ben")
        self.assertNotEqual(get_data()[0], "56789")

    def test_something2(self):
        c = addschooll("kkkkk", "test", 0, 0)
        c.save()
        cc = School.objects.get(name="kkkkk")
        self.assertEqual(cc.town, "test")
        self.assertEqual(cc.x_axis, 0)
        self.assertEqual(cc.y_axis, 0)
        School.objects.get(name="kkkkk").delete()
        cc.delete()
    def test_addmessegerequest(self):
         temp=addmessegerequest("heloo",'hi',1,2)
         temp.save()
         temp2 = messegerequest.objects.get(text="heloo")
         self.assertEqual(temp2.text, "heloo")
         self.assertEqual(temp2.header, "hi")
         self.assertEqual(temp2.urg, True)
         messegerequest.objects.get(text="heloo").delete()
         temp2.delete()
    def test_getemptyschools(self):
        c=getemptyschools()
        self.assertEqual(c[1].coord_id,-1)
    def test_getfullschools(self):
        c=getfullschools()
        self.assertNotEqual(c[0],-1)
    def test_getcoordinators(self):
        c=getcoordinators()
        self.assertEqual(c[0].is_coordinator,True)
        self.assertNotEqual(c[0].is_coordinator,False)
    def test_getaboutus(self):
        self.assertEqual(getaboutus()[0], "hello nice")
        self.assertEqual(getaboutus()[1], "hello for you")
        self.assertNotEqual(getaboutus()[1], "hello for every body3")

    def test_changeaboutus(self):
        changeaboutus("hello nice","hello for you ")
        self.assertEqual(getaboutus()[0],"hello nice")
        self.assertEqual(getaboutus()[1],"hello for you")
        self.assertNotEqual(getaboutus()[1],"hello for every body3")




if __name__ == '__main__':
    unittest.main()
