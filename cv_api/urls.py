from django.urls import path
from .views import EmpDetails, Location, PostStudentSkills, home,InternshipPreferences

urlpatterns = [
    path('home/',home),
    path('PostStudentExternalAchievement/<int:EPUserId>',EmpDetails.as_view()),
    path('PostStudentProfilePreferredLocation/',Location.as_view()),
    path('PostStudentSkill/',PostStudentSkills.as_view()),
    path('PostInternshipPreference/', InternshipPreferences.as_view())
]
