from django.template import response
from django.template.loader import render_to_string
from django.test.runner import DiscoverRunner
from django.urls import reverse

from manager.models import School, contactus

from django.test import TestCase,Client


class Testview(TestCase):
     def setUp(self) -> None:
        self.cred={'username':'adam','password':'12345'}
        self.client=Client()
        self.login=reverse("login")
        self.logout = reverse("logoutUser")
        self.mainpage = reverse('mainpage')
        self.contactus=reverse('contactus')
        self.changepic=reverse('changepic')
        self.addcoor= reverse('addcoordinator')
        self.addschool= reverse('addschool')
        self.urgent=reverse('urgent')
        self.contactuspage=reverse('contactuspage',args=[1])
        self.aboutus=reverse('aboutus')
        self.send_feedback=reverse('send-feedback')
        self.viewfeedbacks=reverse('viewfeedbacks')
        self.oldfeedbacks=reverse('oldfeedbacks')

     #
     # def test_login(self):
     #     self.assertEqual(200, 200)
     #     response=self.client.get(self.login)
     #     self.assertEqual(response.status_code,200)
     #     self.assertTemplateUsed(response,"manager/login.html")
     #
     # def test_logout(self):
     #    response=self.client.get(self.logout)
     #    self.assertEqual(response.status_code,200)
     #    self.assertTemplateUsed(response, "manager/logout.html")
     #    self.assertNotEqual(response.status_code,300)
     # def test_mainpage(self):
     #    response = self.client.post(self.login, self.cred, follow=True)
     #    response = self.client.post(self.mainpage)
     #    self.assertEqual(response.status_code, 200)
     #    self.assertTemplateUsed(response,"manager/base.html")
     #    self.assertNotEqual(response.status_code, 300)
     # def test_addschool(self):
     #       response=self.client.post(self.login,self.cred,follow=True)
     #       response = self.client.get(self.addschool)
     #       self.assertEqual(response.status_code,200)
     #       self.assertTemplateUsed(response,"manager/add_school.html")
     #
     # def test_contactus(self):
     #     response = self.client.post(self.contactus)
     #     self.assertEqual(response.status_code, 200)
     #     self.assertTemplateUsed(response, "mainpage/contactus.html")
     #
     # def test_changepic(self):
     #     response=self.client.get(self.changepic)
     #     self.assertEqual(response.status_code, 200)
     #     self.assertTemplateUsed(response,"manager/base.html")
     # def test_addcoordinator(self):
     #     response = self.client.post(self.login, self.cred, follow=True)
     #     response = self.client.get(self.addcoor)
     #     self.assertEqual(response.status_code, 200)
     #     self.assertTemplateUsed(response, "manager/base.html")
     #     self.assertTemplateUsed(response, "manager/add_coordinator.html")
     # def test_urgent(self):
     #     response = self.client.post(self.login, self.cred, follow=True)
     #     response = self.client.get(self.urgent)
     #     self.assertEqual(response.status_code, 200)
     #     self.assertTemplateUsed(response, "manager/urgent.html")
     #
     #
     # def test_aboutus(self):
     #     response = self.client.post(self.login, self.cred, follow=True)
     #     response = self.client.get(self.aboutus)
     #     self.assertEqual(response.status_code, 200)
     #     self.assertTemplateUsed(response, 'mainpage/About_us.html')
     #
     # def test_send_feedback(self):
     #    response = self.client.post(self.login, self.cred, follow=True)
     #    response = self.client.get(self.send_feedback)
     #    self.assertEqual(response.status_code, 200)
     #    self.assertTemplateUsed(response, 'manager/send_feedback.html')
     #    self.assertNotEqual(response.status_code,234)
     #
     # def test_viewfeedbacks(self):
     #    response = self.client.post(self.login, self.cred, follow=True)
     #    response = self.client.get(self.viewfeedbacks)
     #    self.assertEqual(response.status_code, 200)
     #    self.assertTemplateUsed(response, 'manager/view_feedbacks.html')
     #    self.assertNotEqual(response.status_code,234)
     # def test_oldfeedbacks(self):
     #     response = self.client.post(self.login, self.cred, follow=True)
     #     response = self.client.get(self.oldfeedbacks)
     #     self.assertEqual(response.status_code, 200)
     #     self.assertTemplateUsed(response, 'manager/old_feedbacks.html')
     #     self.assertNotEqual(response.status_code, 234)

     def test_oldfeedbacks2(self):
         response = self.client.post(self.login, self.cred, follow=True)
         response = self.client.get(self.oldfeedbacks)
         self.assertEqual(response.status_code, 200)
         self.assertTemplateUsed(response, 'manager/old_feedbacks.html')
         self.assertNotEqual(response.status_code, 234)


if __name__ == '__main__':

   TestCase.main()


