from django.db import models

# Create your models here.
# tocreate table name with data base columns 
class Employee(models.Model):
    name = models.CharField('name',max_length=50)
    mobile = models.CharField('mobile',max_length=12)
    address = models.CharField('address',max_length=100)
    email = models.CharField('email',max_length=30)
    designation = models.CharField('designation',max_length=20)

    def __str__(self):
        return self.name