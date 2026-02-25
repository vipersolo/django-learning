from django.test import TestCase
from .models import Student

# Create your tests here.

class StudentModelTest(TestCase):
    def setUp(self): #case sensitive 
        self.student1  = Student.objects.create(
            name = "Antony",
            email = "antony@example.com"
        )

    def teststudentcreation(self):
        self.assertEqual(self.student1.name,"Antony")
        self.assertEqual(self.student1.email,"antony@example.com")
        self.assertIsNotNone(self.student1.created_at)

    def test_str_method(self):
        self.assertEqual(str(self.student1),"Antony")

    def test_email_unique(self):
        with self.assertRaises(Exception):
            Student.objects.create(
                name = "kuku",
                email = "antony@example.com"
            )