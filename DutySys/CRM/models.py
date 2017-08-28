from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uid=models.AutoField(primary_key=True)
    username=models.CharField(max_length=32)
    pwd=models.CharField(max_length=64)
    r_action=models.ManyToManyField("ActionInfo")

class TestInfo(models.Model):
    testname=models.CharField(max_length=64)

class ActionInfo(models.Model):
    aid=models.AutoField(primary_key=True)
    actionName=models.CharField(max_length=128)
    url=models.CharField(max_length=64)
