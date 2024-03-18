from django.shortcuts import render

# start
from django.http import JsonResponse ,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics , permissions
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .serializers import UserCreateSerializer, CourseSerializer , InstructorSerializer , ModuleSerializer , VideoSerializer , WorkBookSerializer , QuizSerializer , QuizQuestionSerializer, EnrollmentSerializer,RoleSerializer
from .import models
from rest_framework import viewsets
# #  end

class UserCreateList(generics.ListCreateAPIView): 
    queryset = models.UserAccounts.objects.all() 
    serializer_class= UserCreateSerializer
    # permission_classes = [permissions.IsAuthenticated]
    # @csrf_exempt 
    # def student_login(request): 
    #     email = request.POST['email'] 
    #     password =request.POST['password'] 
    #     try: 
    #         studentData = models.UserAccounts.objects.get(email =email , password =password) 
    #     except models.UserAccounts.DoesNotExist: 
    #         studentData = None 
            
    #     if studentData: 
    #         return JsonResponse({'bool':True,'id':studentData.id})             
    #     else: 
    #         return JsonResponse({'bool': False}) 
# Create your views here.
class ModuleList(generics.ListCreateAPIView): 
    queryset =models.Module.objects.all() 
    serializer_class = ModuleSerializer 

class CourseViewList(generics.ListCreateAPIView): 
    queryset =models.Course.objects.all() 
    serializer_class = CourseSerializer 
    
    # permission_classes = [permissions.IsAuthenticated]
class RoleViewList(generics.ListCreateAPIView): 
    queryset = models.Role.objects.all()  
    serializer_class = RoleSerializer


     
# class CourseContentList(generics.ListCreateAPIView): 
#     queryset = models.CourseContent.objects.all() 
#     serializer_class = CourseSerializer 
class EnrollmentList(generics.RetrieveUpdateDestroyAPIView): 
    queryset = models.Enrollment.objects.all() 
    serializer_class = EnrollmentSerializer 
     
# class ReviewList(generics.ListCreateAPIView): 
#     queryset = models.Review.objects.all() 
#     serializer_class = ReviewSerializer 
     
class InstructorList(generics.ListCreateAPIView): 
    queryset = models.Instructor.objects.all() 
    serializer_class = InstructorSerializer 
# class InstructorDetail(generics.RetrieveUpdateDestroyAPIView): 
#     queryset = models.Instructor.objects.all() 
#     serializer_class = InstructorSerializer 
#     # def get_object(self): 
#     #     obj = super().get_object() 
#     #     # print("obj",obj) 
#     #     course= self.kwargs["course"] 
#     #     # print("course",course)     

 
class WorkbookList(generics.ListCreateAPIView): 
    queryset = models.WorkBook.objects.all() 
    serializer_class = WorkBookSerializer 
     
class VideoList(generics.ListCreateAPIView): 
    queryset = models.Video.objects.all() 
    serializer_class = VideoSerializer    
     
class QuizList(generics.ListCreateAPIView): 
    queryset = models.Quiz.objects.all() 
    serializer_class = QuizSerializer 
     
class QuizQuestionList(generics.ListCreateAPIView): 
    queryset = models.QuizQuestions.objects.all() 
    serializer_class = QuizQuestionSerializer  
     
    def get_queryset(self): 
        quiz_id =self.kwargs['quiz_id'] 
        quiz =models.Quiz.objects.get(pk=quiz_id) 
        return models.QuizQuestions.objects.filter(quiz=quiz)