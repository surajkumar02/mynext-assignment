from django.contrib import admin
from .models import InternshipPreferenceModel,SkillsModel,LocationModel,EmpDetailsModel

# Register your models here.

admin.site.register(InternshipPreferenceModel)
admin.site.register(SkillsModel)
admin.site.register(LocationModel)
admin.site.register(EmpDetailsModel)
