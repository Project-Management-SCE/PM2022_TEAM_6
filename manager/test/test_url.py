from django.template import response
from django.template.loader import render_to_string
from django.test.runner import DiscoverRunner
from django.urls import reverse,resolve

from mainpage.views import about_us, contact_us
from manager.models import School, contactus

from django.test import TestCase,Client

from manager.views import loginPage, logoutUser, mainpage, addschool, add_coordinator, urgentrequest, changepic, \
    feedback_view, oldfeedbacks, send_feedback, aboutus, contactuspage, spfeedback


class test_urls_manager(TestCase):
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
    def test_send_feedbacks_url_is_resloved(self):
        url = reverse('send-feedback')
        self.assertEqual(resolve(url).func,send_feedback)
        self.assertNotEqual(resolve(url).func, addschool)

    def test_oldfeedbacks_url_is_resloved(self):
        url = reverse('oldfeedbacks')
        self.assertEqual(resolve(url).func,oldfeedbacks)
        self.assertNotEqual(resolve(url).func, addschool)

    def test_viewfeedbacks_url_is_resloved(self):
        url = reverse('viewfeedbacks')
        self.assertEqual(resolve(url).func, feedback_view)
        self.assertNotEqual(resolve(url).func, addschool)
    def test_aboutus_url_is_resloved(self):
        url = reverse('aboutus')
        self.assertEqual(resolve(url).func, about_us)
        self.assertNotEqual(resolve(url).func, addschool)

    def test_contactus_url_is_resloved(self):
        url = reverse('contactus')
        self.assertEqual(resolve(url).func,contact_us)
        self.assertNotEqual(resolve(url).func, about_us)

    def test_contactuspage_url_is_resloved(self):
        url = reverse('contactuspage',args=[1])
        self.assertEqual(resolve(url).func, contactuspage)
        self.assertNotEqual(resolve(url).func, contact_us)

    def test_spfeedback_url_is_resloved(self):
        url = reverse('spfeedback',args=[1])
        self.assertEqual(resolve(url).func, spfeedback)
        self.assertNotEqual(resolve(url).func, contact_us)

