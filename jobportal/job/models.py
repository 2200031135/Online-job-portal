# your_app/models.py

from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Add other fields like location, company, etc.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



# Create your models here.
class Userregistration(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def str(self):
        return self.username

class adminlogin(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def str(self):
        return self.username

class recruiterlogin(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def str(self):
        return self.username

class applylogin(models.Model):
    id=models.AutoField(blank=False,primary_key=True)
    username = models.CharField(max_length=50,blank=False)
    email = models.EmailField(max_length=50,blank=False)
    password = models.CharField(max_length=20)
    repassword = models.CharField(max_length=20)

    def str(self):
        return self.username


