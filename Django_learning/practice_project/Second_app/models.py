from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#One to Many relationship in model

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  
    review_text = models.TextField()
    rating = models.IntegerField()

# many to many relationship in model

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')

# one to one relationship in model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    bio = models.TextField()
