from django.test import TestCase

from manager.models import messegerequest, School, contactus, logs, feedbacks, schoolrequest, volinstances


class test_modeles(TestCase):
    def setUp(self) -> None:
        self.messegerequest1=messegerequest.objects.create(text='hello',header='higys',urg=False,volid=2)
        self.School1=School.objects.create(name='samr',town="bearshiva",x_axis=34.456,y_axis=34.553,coord_id=4)
        self.contactus1=contactus.objects.create(name="sdd",cons="sad",text="asdas")
        self.logs1=logs.objects.create(activity="addd",done_by=3,done_to=2)
        self.feedbacks1=feedbacks.objects.create(is_read=False,reciever_id=3,sender_id=2,text="nice",header="no",urg=True)
        self.schoolrequest1=schoolrequest.objects.create(accepted=True,school_id=2,volnteer_id=3,volnteer_name="sss")
        self.volinstances1=volinstances.objects.create(title="check",description="check2",school_id=2,cor_id=1,complete=True)

    def test_messegerequest(self):
        self.assertEqual(self.messegerequest1.text,'hello')
        self.assertEqual(self.messegerequest1.header,'higys')
        self.assertEqual(self.messegerequest1.urg,False)
    def test_School(self):
        self.assertEqual(self.School1.name, 'samr')
        self.assertEqual(self.School1.town, 'bearshiva')
        self.assertEqual(self.School1.x_axis, 34.456)
        self.assertEqual(self.School1.y_axis, 34.553)
    def test_contactus(self):
        self.assertEqual(self.contactus1.name,'sdd')
        self.assertEqual(self.contactus1.cons,'sad')
        self.assertEqual(self.contactus1.text,'asdas')
    def test_logss(self):
        self.assertEqual(self.logs1.activity, 'addd')
        self.assertEqual(self.logs1.done_by, 3)
        self.assertEqual(self.logs1.done_to, 2)
    def test_feedbacks(self):
        self.assertNotEqual(self.feedbacks1.is_read, True)
        self.assertEqual(self.feedbacks1.reciever_id, 3)
        self.assertEqual(self.feedbacks1.sender_id, 2)
        self.assertEqual(self.feedbacks1.text, "nice")
        self.assertEqual(self.feedbacks1.header, "no")
    def test_volinstances(self):
        self.assertEqual(self.volinstances1.title,"check")
        self.assertEqual(self.volinstances1.description,"check2")
        self.assertEqual(self.volinstances1.school_id,2)
        self.assertEqual(self.volinstances1.cor_id,1)
        self.assertEqual(self.volinstances1.complete,True)


