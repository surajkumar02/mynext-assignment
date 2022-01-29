from django.db import models

# Create your models here.

class InternshipPreferenceModel(models.Model):
    st_profile_id=models.IntegerField(null=False)
    available=models.BooleanField()
    end_data=models.DateTimeField()
    university=models.BooleanField()
    start_data=models.DateTimeField()
    student_preferred=models.IntegerField()

class LocationModel(models.Model):
    country_id=models.IntegerField() #foreignkey -all
    student_id=models.ForeignKey(InternshipPreferenceModel, on_delete=models.CASCADE)
    state_id=models.IntegerField() #foreignkey -all
    id=models.AutoField(primary_key=True) #foreignkey -all
    city=models.CharField(max_length=100)
    compensation=models.IntegerField(null=True) #foreignkey with Range id

class SkillsModel(models.Model):
    student_id=models.IntegerField()
    tools_id=models.IntegerField()
    skill_name=models.CharField(max_length=50)


class EmpDetailsModel(models.Model):
    role=models.CharField(max_length=100)
    organisation=models.CharField(max_length=120)
    location=models.CharField(max_length=100)
    duration_start=models.DateTimeField()
    duration_end=models.DateTimeField()