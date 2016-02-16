from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

# TODO: Orange and blue stuff
ACTIVITY_KIND_CHOICES = {
    ('HELP_SELF', 'Helping self'),
    ('HELP_OTHERS', 'Helping others'),
    # Admin option, e.g. for replenishing parts?
}

BIKE_KIND_CHOICES = {
    ('PB', 'Personal bike'),
    ('SB', 'Shop bike'),
    ('SCRAP', 'To be scrapped'),
}

class Bike(models.Model):
    shop_number = models.CharField(max_length=100)
    identifying_info = JSONField()
    photo = models.ImageField()
    kind = models.CharField(max_length=20, choices=BIKE_KIND_CHOICES)

class Person(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    contact_info = JSONField()
    photo = models.ImageField()
    availability = models.TextField()
    interests = models.TextField()
    class Meta:
        abstract = True

class Youth(Person):
    # TODO: record whether the Youth (independent of Person/User) is active
    # If inactive, record reason why? One example could be the Youth is now an
    # Adult, in which case there would be both a Youth (inactive) and an Adult
    # (active) pointing to the same Person
    signed_form = models.BooleanField(default=False)

class Adult(Person):
    # TODO: Any adult-specific fields?
    pass

class Stand(models.Model):
    number = models.CharField(max_length=100)
    # x, y position? Phil's idea of mapping the shop

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'skill categories'
    
class Skill(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(SkillCategory)

class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    consumable = models.BooleanField()
    low_stock = models.BooleanField()

class Activity(models.Model):
    description = models.CharField(max_length=500)
    kind = models.CharField(max_length=20, choices=ACTIVITY_KIND_CHOICES)
    bike = models.ForeignKey(Bike)
    youth = models.ForeignKey(Youth)
    adult = models.ForeignKey(Adult)
    stand = models.ForeignKey(Stand)
    skills = models.ManyToManyField(Skill)
    parts = models.ManyToManyField(Part, through='ActivityPartCount')
    timestamp = models.DateTimeField()
    class Meta:
        verbose_name_plural = 'activities'

class ActivityPartCount(models.Model):
    activity = models.ForeignKey(Activity)
    part = models.ForeignKey(Part)
    count = models.IntegerField()
    # Just make consumption negative and have the UI hand-hold?
    added_to_inventory = models.BooleanField(default=False)

'''
class Job(models.Model):
    skills = models.ManyToManyField(Skill)
    parts = models.ManyToManyField(Part)

class Transaction(Bike(models.Model):
    pass
''' 
