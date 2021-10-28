from django.db import models
from rest_framework.serializers import  ModelSerializer

from UserApi.models import Faculty


class FacultySerializers(ModelSerializer) :
    class Meta:
        fields = ["faculty_name","faculty_ratings","faculty_category","faculty_speciality","faculty_id","faculty_call_charges",'faculty_online']
        model = Faculty