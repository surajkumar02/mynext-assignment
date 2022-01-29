from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView, Response
from .models import InternshipPreferenceModel,SkillsModel,LocationModel,EmpDetailsModel


# Create your views here.

def home(request):
    if request.method =="GET":
        return HttpResponse("Data is here")

class InternshipPreferences(APIView):

    def get(self,request):
       
        return Response({'data':request.data})

    def post(self,request):
        available=request.data['AvailableForInternship']
        end_data=request.data['EndDate']
        university=request.data['IsUniversityProvideInternship']
        start_data=request.data['StartDate']
        student_preferred=request.data['StudentInternshipPreferencesId']
        st_profile_id=request.data['StudentProfileId']

        intern,newintern=InternshipPreferenceModel.objects.get_or_create(st_profile_id=st_profile_id,
                        available=available,start_data=start_data,
                        end_data=end_data,university=university,
                        student_preferred=student_preferred)
        if newintern:
            return Response(data={'message':'New Instance created'})

        return Response(data={'message':'Data is not valid'})

class PostStudentSkills(APIView):
    def get(self,request):
        return Response('Data of Post')

    def post(self,request):
        skill_name=request.data['CustomSkillName']
        student_id=request.data['EPUserId']
        tools_id=request.data['ToolsAndTechnologyId']
        skills,newskills=SkillsModel.objects.get_or_create(student_id=student_id,
                         skill_name=skill_name,tools_id=tools_id)
        if newskills:
            return Response(data={'message':"New Instance created"})
        return Response(data={"Here is all data"})

class Location(APIView):
    def get(self,request):
        print(request.GET['studentId'])
        return Response('Data of Location')

    def post(self,request):
        # val=request.params['profileId']
        student_id=request.GET['studentId']
        country_id=request.data['CountryId']
        state_id=request.data['StateId']
        city=request.data['City']
        location,newlocation=LocationModel.objects.get_or_create(student_id=student_id,
                                country_id=country_id,state_id=state_id,
                                city=city)
        if newlocation:
            return Response('New Instance created')
        return Response(data={"Here is all data"})

class EmpDetails(APIView):
    def get(self,request):
        return Response('Data of Emp Details')

    def post(self,request,EPUserId=None):
        print(EPUserId)
        
        role=request.data['AchievementTitle']
        organisation=request.data['Company']
        location=request.data['Location']
        duration_start=request.data['StartDate']
        duration_end=request.data['EndDate']
        emp,newemp=EmpDetailsModel.objects.get_or_create(role=role,
                    organisation=organisation,location=location,
                    duration_start=duration_start,duration_end=duration_end)
        if newemp:
            return Response('New Instance Created')
        return Response(data={"Data is not valid"})