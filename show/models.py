from django.db import models

# Create your models here.
class B(models.Model):
    direction = models.CharField( max_length=200)
    dir_type = models.IntegerField(default=0)
class M(models.Model):
    department = models.CharField( max_length=200)
    dep_type = models.IntegerField(default=0)
class S(models.Model):
    school = models.CharField(max_length=200)
    sch_type = models.IntegerField(default=0)
class Sest(models.Model):
    option = models.CharField(max_length=200)
