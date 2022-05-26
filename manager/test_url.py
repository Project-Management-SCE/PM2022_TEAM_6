from django.template import response
from django.template.loader import render_to_string
from django.test.runner import DiscoverRunner
from django.urls import reverse,resolve

from mainpage.views import about_us, contact_us
from manager.models import School, contactus

from django.test import TestCase,Client

from manager.views import loginPage, logoutUser, mainpage, addschool, add_coordinator, urgentrequest, changepic, \
    feedback_view, oldfeedbacks, send_feedback, aboutus, contactuspage, spfeedback


class test_urls(TestCase):
    def test_login_url_is_resloved(self):
        url=reverse('login')
        self.assertEqual(resolve(url).func,loginPage)

    def test_logoutUser_url_is_resloved(self):
        url = reverse('logoutUser')
        self.assertEqual(resolve(url).func, logoutUser)

    def test_mainpage_url_is_resloved(self):
        url = reverse('mainpage')
        self.assertEqual(resolve(url).func, mainpage)

    def test_addschool_url_is_resloved(self):
        url = reverse('addschool')
        self.assertEqual(resolve(url).func, addschool)

    def test_addcoordinator_url_is_resloved(self):
        url = reverse('addcoordinator')
        self.assertEqual(resolve(url).func, add_coordinator)

    def test_urgent_url_is_resloved(self):
        url = reverse('urgent')
        self.assertEqual(resolve(url).func, urgentrequest)
        self.assertNotEqual(resolve(url).func, addschool)
        self.assertEqual(2,2)

    def test_changepic_url_is_resloved(self):
        url = reverse('changepic')
        self.assertEqual(resolve(url).func, changepic)
        self.assertNotEqual(resolve(url).func,addschool)

