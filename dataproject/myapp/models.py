from django.db import models
from django.contrib import admin
# Create your models here.
class Employee(models.Model):
    emp_id=models.CharField(max_length=20,primary_key=True)
    ename=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    post=models.CharField(max_length=20)
    salary=models.IntegerField()

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('emp_id','ename','lastname','post','salary')