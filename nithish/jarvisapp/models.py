from django.db import models
from django.contrib import admin

class Vehicle_DB(models.Model):
    Complaints = models.TextField()
    Vehicle_Name = models.CharField(max_length=10)
    Purchase_Date = models.DateField()
    Email = models.EmailField()
    Address = models.TextField()
    RC_Number = models.CharField(max_length=10, primary_key=True)
    DL_Number = models.CharField(max_length=12)

class Vehicle_DBAdmin(admin.ModelAdmin):
    list_display = ["Complaints", "Vehicle_Name", "Purchase_Date", "Email", "Address", "RC_Number", "DL_Number"]