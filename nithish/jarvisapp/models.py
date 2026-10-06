from django.db import models
from django.contrib import admin
class student_DB(models.Model):
    REf_No=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=10)
    DoB=models.DateField()
    Email=models.EmailField()
    Address=models.TextField()
    Mobile=models.IntegerField()
    percentage=models.FloatField()
class student_DBAdmin(admin.ModelAdmin):
    list_display=["REf_No","Name","DoB","Email","Address"]