from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10)

class Teacher(models.Model):
    name = models.CharField(max_length=100)
  
class Parent(models.Model):
    name = models.CharField(max_length=100)
    children = models.ManyToManyField(Student, related_name='parents')
    