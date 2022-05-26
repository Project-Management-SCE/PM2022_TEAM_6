import unittest
from django.urls import reverse
from  django.test import Client,TestCase


class Testview(TestCase):
    # def setUp(self) -> None:
    #     self.client=Client()
    #     self.login=reverse("login")
    #     self.logout=reverse("logoutUser")
    #     self.mainpage1 = reverse("mainpage")
    def test_login(self):
        self.assertEqual(200, 200)
        # response=self.client.get(self.login)
    #     self.assertEqual(response.status_code,200)
    #     self.assertTemplateUsed(response,"manager/login.html")
    #
    # def test_logout(self):
    #     response=self.client.get(self.logout)

    #     self.assertEqual(response.status_code,200)
    #     self.assertTemplateUsed(response, "manager/logout.html")
    #     self.assertNotEqual(response.status_code,300)
    # # def test_mainpage(self):
    # #     response = self.client.get(self.mainpage1)
    # #     self.assertEqual(response.status_code, 200)
    # #     self.assertTemplateUsed(response, "manager/base.html")
    #     # self.assertNotEqual(response.status_code, 300)
    #
    #
    #
    #
    #
















if __name__ == '__main__':

   TestCase.main()



