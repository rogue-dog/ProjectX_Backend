from datetime import datetime
from django.db import models
from django.db.models.expressions import Value
from django.core.validators import validate_comma_separated_integer_list
from django.db.models.query_utils import DeferredAttribute
import uuid

# Create your models here.


class User(models.Model):
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)


class UserVerification(models.Model):
    email = models.CharField(max_length=250, primary_key=True)
    otp = models.CharField(max_length=4)

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=250)
    faculty_speciality = models.CharField(max_length=250)
    faculty_id = models.UUIDField(default=uuid.uuid5,primary_key=True)
    faculty_call_charges = models.IntegerField()
    
    faculty_ratings =models.IntegerField()
    faculty_category = models.CharField(max_length=240)
    faculty_online = models.BooleanField(default=True)
