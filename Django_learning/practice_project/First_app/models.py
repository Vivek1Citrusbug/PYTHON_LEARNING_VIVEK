from django.db import models

# # Create your models here.
class students(models.Model):
    student_name = models.CharField(max_length=50)
    student_id = models.IntegerField()
    join_date = models.DateField(auto_now=False, auto_now_add=False)
    result = models.CharField(max_length=50)
