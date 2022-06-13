from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):#OK
    user_id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True)
    user = models.TextField(blank=True, null=False)
    password = models.TextField(blank=True, null=False)
    email = models.TextField(blank=True, null=False)
    groups = models.TextField(blank=True, null=False)
    region = models.TextField(blank=True, null=False)
    record = models.TextField(blank=True, null=False)
    description = models.TextField(blank=True, null=False)
    setting = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.user

class Test(models.Model):
    one = models.TextField(blank=True, null=False)
    two = models.TextField(blank=True, null=False)
    three = models.TextField(blank=True, null=False)
    four = models.TextField(blank=True, null=False)
    five = models.TextField(blank=True, null=False)
    class Meta:
        db_table = 'test'

    def __str__(self):
        return self.one

class Product(models.Model):
    id = models.IntegerField(db_column='id', unique=True, blank=True, null=False, primary_key=True)
    name = models.TextField(blank=True)
    price = models.IntegerField(blank=True)
    amount = models.IntegerField(blank=True)
    hot = models.IntegerField(blank=True)
    time = models.TextField(blank=True)
    owner = models.TextField(blank=True)
    group = models.TextField(blank=True)
    url = models.TextField(blank=True)
    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
