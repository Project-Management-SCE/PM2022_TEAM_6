from django.template import response
from django.template.loader import render_to_string
from django.test.runner import DiscoverRunner
from django.urls import reverse,resolve


from django.test import TestCase,Client

from voulnteers.views import createaccount, index1, requestpage, showschools, logoutvoulnteer, changepic1, schoolinfo, \
    feedback_view1,mainpage1


class test_urls_voulnteers(TestCase):
    def test_index_url_is_resloved(self):
        url=reverse('index1')
        self.assertEqual(resolve(url).func,index1)
        self.assertNotEqual(resolve(url).func,createaccount)
    def test_createaccount_url_is_resloved(self):
        url=reverse('createaccount')
        self.assertEqual(resolve(url).func,createaccount)
        self.assertNotEqual(resolve(url).func,index1)
    def test_mainpage_url_is_resloved(self):
        url=reverse('mainpage1')
        self.assertEqual(resolve(url).func,mainpage1)
        self.assertNotEqual(resolve(url).func,index1)
    def test_schools_url_is_resloved(self):
        url=reverse('schools')
        self.assertEqual(resolve(url).func,showschools)
        self.assertNotEqual(resolve(url).func,createaccount)
    def test_request_url_is_resloved(self):
        url=reverse('requeset')
        self.assertEqual(resolve(url).func,requestpage)
        self.assertNotEqual(resolve(url).func,createaccount)
    def test_logoutvoulnteer_url_is_resloved(self):
        url=reverse('logoutvoulnteer')
        self.assertEqual(resolve(url).func,logoutvoulnteer)
        self.assertNotEqual(resolve(url).func,createaccount)
    def test_changepic_url_is_resloved(self):
        url=reverse('changepic1')
        self.assertEqual(resolve(url).func,changepic1)
        self.assertNotEqual(resolve(url).func,createaccount)
    def test_schoolinfo_url_is_resloved(self):
        url=reverse('schoolinfo',args=[1])
        self.assertEqual(resolve(url).func,schoolinfo)
        self.assertNotEqual(resolve(url).func,createaccount)
    def test_feedback_view_url_is_resloved(self):
        url=reverse('viewfeedbacks1')
        self.assertEqual(resolve(url).func,feedback_view1)
        self.assertNotEqual(resolve(url).func,createaccount)
