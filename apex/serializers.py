from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers 
from .import models 
 
User = get_user_model()
class UserCreateSerializer (UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model =User
        fields=('id', 'email','first_name','middle_name', 'last_name','user_name','role' ,'password')
        depth= 1
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Module
        fields = ['module_id','module_name']  
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"
     
        
                
class CourseSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = models.Course 
        fields =['id' ,'featured_img','course_name','title' ,'features','module','price'] 
     
        
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields = ['id','name','gender','email','phone_number'] 
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Video
        fields = ['id','title','description','video_file','module']        
class WorkBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorkBook
        fields =['id ','title','description','pdf_file','module'] 
         
         
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quiz
        fields =['id','title','questions','module']  
        depth = 1
       
        
        
class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuizQuestions
        fields =['id','quiz','questions','ans1','ans2','ans3','ans4','right_ans','add_time']
        depth=2

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Enrollment
        fields = ['course','rating','reviews']
                      
             