from django.db import models

class WorkExperience(models.Model):
    Company_Name = models.CharField(max_length = 100)
    From_date    = models.DateField()
    To_Date      = models.DateField()
    address      = models.TextField(max_length=50)

class Address(models.Model):
    hno = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)    

class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100)
    percentage = models.FloatField()

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='project_photos/')

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)
    work_experience = models.ManyToManyField(WorkExperience)
    qualifications = models.ManyToManyField(Qualification)
    projects = models.ManyToManyField(Project)        