from django.db import models
# Create your models here.
#abstract type inheritance
class ContactInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
    class Meta:
        abstract = True
class Student(ContactInfo):
    rollno = models.IntegerField()
    marks = models.IntegerField()
class Teacher(ContactInfo):
    subject = models.CharField(max_length=30)
    salary = models.FloatField()

#multi-table inheritance
class ContactInfo1(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=30)
class Student1(ContactInfo1):
    rollno = models.IntegerField()
    marks = models.IntegerField()
class Teacher1(ContactInfo1):
    subject = models.CharField(max_length=30)
    salary = models.FloatField()