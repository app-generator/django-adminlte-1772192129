# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Department(models.Model):

    #__Department_FIELDS__
    department_id = models.IntegerField(null=True, blank=True)
    department_name = models.CharField(max_length=255, null=True, blank=True)

    #__Department_FIELDS__END

    class Meta:
        verbose_name        = _("Department")
        verbose_name_plural = _("Department")


class Employees(models.Model):

    #__Employees_FIELDS__
    employee_id = models.IntegerField(null=True, blank=True)
    employee_name = models.TextField(max_length=255, null=True, blank=True)
    department_id = models.IntegerField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    hiring_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Employees_FIELDS__END

    class Meta:
        verbose_name        = _("Employees")
        verbose_name_plural = _("Employees")



#__MODELS__END
