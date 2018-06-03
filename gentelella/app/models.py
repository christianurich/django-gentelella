from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Resource(models.Model):
    SKILLTYPES = (
        ('economics', 'economics'),
        ('urban climate', 'urban climate'),
        ('wastewater', 'wastewater'),
        ('urban design', 'urban design'),
        ('urban planning and governance', 'urban planning and governance'),
        ('engagement and behaviour change', 'engagement and behaviour change'),
        ('integrated systems modelling', 'integrated systems modelling'),
        ('transition strategy development', 'trasnsition strategy development'),
        ('urban hydrology and flooding', 'urban hydrology and flooding'),
        ('green infrastructure', 'green infrastructure'),
        ('process design', 'process design'),
        ('service delivery manager', 'service delivery manager'),
        ('senior academic', 'senior academic'),
        ('admin/comms', 'admin/comms'),
        ('rs facilitation', 'rs facilitation'),
        ('project managment', 'project management'),
        ('town planning', 'town planning'),
        ('urban ecology', 'urban ecology'),
        ('wsc-i application', 'wsc-i application'),
        ('senior industry expert', 'senior industry expert'),
        ('admin contract', 'admin contract'),
        ('other external', 'other external'))


    skill = models.CharField(max_length=100, choices=SKILLTYPES)
    existing_fte_days = models.FloatField(null=True)
    fte_pax = models.FloatField(null=True)
    int_ext = models.CharField(max_length=3)  # internal or external
    daily_cost = models.FloatField()

    def __str__(self):
        return self.skill


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.last_name} ({self.email})"


class Project(models.Model):
    POTYPES = (
        ('RAE', 'RAE'),
        ('COO', 'COO'),
        ('CRO', 'CRO'),
        ('CEO', 'CEO'))


    title = models.CharField(max_length=200)
    code = models.CharField(max_length=6)
    location = models.CharField(max_length=30)
    funding_cat = models.CharField(max_length=30)
    portfolio_owner = models.CharField(max_length=3, choices=POTYPES)
    leader = models.CharField(max_length=50, blank=True)
    initiator = models.ManyToManyField(Employee, blank=True, related_name="users")
    certainty = models.IntegerField()
    category = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    experts = models.ManyToManyField(Resource, blank=True, related_name="skills")
    exp_specialists = models.FloatField(null=True)
    exp_other = models.FloatField(null=True)
    inflow_crc = models.FloatField(null=True)
    inflow_ext = models.FloatField(null=True)



    required_funds = models.FloatField(null=True)
    profit_margin = models.FloatField(null=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.code
