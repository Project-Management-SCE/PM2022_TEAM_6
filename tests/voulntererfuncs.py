import sys
from django.test import TestCase
import unittest
from voulnteers.models import  volnteer

sys.path.append('../')
from funcs.voulnteerfuncs import addvoulnteer,getvolname,checkpic

class TestModel(unittest.TestCase):

    def test_addvoulnteer(self):
        test=addvoulnteer("sami","hamad1997m@gmail.com","2123")
        testbase = volnteer.objects.get(username="sami")
        self.assertEqual( testbase.username,"sami")
        self.assertEqual(testbase.password, "2123")
        self.assertNotEqual(testbase.username,"sami2")
        testbase.delete()

    def test_getvolname(self):
        test=getvolname(75)
        testbase=volnteer.objects.get(id=75)
        self.assertEqual(testbase.username, test)
    def test_checkpic(self):
        self.assertEqual(True,checkpic("jpg"))
        self.assertNotEqual(True,checkpic("mp4"))





if __name__ == '__main__':
    unittest.main()
