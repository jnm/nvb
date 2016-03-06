from __future__ import unicode_literals

import datetime

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

# Create your models here.

# TODO: Orange and blue stuff
SHOP_SESSION_KIND_CHOICES = {
    ('HELP_SELF', 'Helping self'),
    ('HELP_OTHERS', 'Helping others'),
}

class Person(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    contact_info = JSONField()
    photo = models.ImageField()
    availability = models.TextField()
    interests = models.TextField()
    def __unicode__(self):
        return self.user.__unicode__()


class Youth(Person):
    # TODO: record whether the Youth (independent of Person/User) is active
    # If inactive, record reason why? One example could be the Youth is now an
    # Adult, in which case there would be both a Youth (inactive) and an Adult
    # (active) pointing to the same Person
    signed_form = models.BooleanField(default=False)
    def __unicode__(self):
        return 'YOUTH: {}'.format(super(Youth, self).__unicode__())


class Adult(Person):
    def __unicode__(self):
        return 'ADULT: {}'.format(super(Youth, self).__unicode__())


class Bike(models.Model):
    name = models.CharField(max_length=100, blank=True)
    when_added = models.DateTimeField(default=datetime.datetime.now)
    shop_number = models.CharField(max_length=100, blank=True)
    identifying_info = JSONField()
    photo = models.ImageField()
    owner = models.ForeignKey(Person, blank=True, null=True)
    for_scrap = models.BooleanField(default=False)
    # Perhaps more of a to-do list than a list of past activites; make it a
    # JSONField so Philip can do something interesting with it
    history = JSONField()
    @property
    def kind(self):
        return 'PB' if self.owner else 'SB'

    # If the bike has an owner, it's a PB. Otherwise, it's an SB.
    def __unicode__(self):
        return '{}: {} ({})'.format(self.kind, self.name, self.shop_number)


class Stand(models.Model):
    number = models.CharField(max_length=100)
    # x, y position? Phil's idea of mapping the shop
    def __unicode__(self):
        return 'Stand {}'.format(self.number)


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'skill categories'
    def __unicode__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(SkillCategory)
    def __unicode__(self):
        return '{}: {}'.format(self.category.name, self.name)


class Part(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)
    consumable = models.BooleanField(default=False)
    def __unicode__(self):
        return self.name


class ShopSession(models.Model):
    person = models.ForeignKey(Person)
    mood = models.CharField(max_length=100, blank=True)
    time_in = models.DateTimeField(default=datetime.datetime.now)
    time_out = models.DateTimeField(blank=True, null=True)
    kind = models.CharField(max_length=20, choices=SHOP_SESSION_KIND_CHOICES)
    stand = models.ForeignKey(Stand, blank=True, null=True)
    def __unicode__(self):
        return '{}: {}'.format(self.person.__unicode__(), self.kind)


class Activity(models.Model):
    description = models.CharField(max_length=500, blank=True)
    shop_session = models.ForeignKey(ShopSession)
    approver = models.ForeignKey(Adult, blank=True, null=True)
    bike = models.ForeignKey(Bike, blank=True, null=True)
    skills = models.ManyToManyField(Skill, through='ActivitySkill')
    parts = models.ManyToManyField(Part, through='ActivityPart')
    class Meta:
        verbose_name_plural = 'activities'
    # TODO: __unicode__ method


class ActivitySkill(models.Model):
    activity = models.ForeignKey(Activity)
    skill = models.ForeignKey(Skill)
    acquired = models.BooleanField(default=False)

class ActivityPart(models.Model):
    activity = models.ForeignKey(Activity)
    part = models.ForeignKey(Part)
    # Don't require in case an unquantifiable amount was used
    quantity_used = models.IntegerField(blank=True, null=True)
    # For parts that may not have a definite quantity, allow flagging when
    # stock runs low
    low_stock = models.BooleanField(default=False)
