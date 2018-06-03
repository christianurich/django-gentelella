from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    location = models.CharField(max_length=30)
    funding_cat = models.CharField(max_length=30)
    portfolio_owner = models.CharField(max_length=3)
    leader = models.CharField(max_length=50)
    initiator = models.CharField(max_length=50)
    certainty = models.IntegerField()
    category = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    exp_specialists = models.FloatField()
    exp_other = models.FloatField()
    inflow_crc = models.FloatField()
    inflow_ext = models.FloatField()
    reqd_funds = models.FloatField()
    profit_margin = models.FloatField()
    comments = models.TextField()

    def __str__(self):
        return self.code


class Resource(models.Model):
    skill = models.CharField(max_length=100)
    existing_fte_days = models.FloatField()
    fte_pax = models.FloatField()
    int_ext = models.CharField(max_length=3)  # internal or external
    daily_cost = models.FloatField()

    def __str__(self):
        return self.skill


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.last_name
