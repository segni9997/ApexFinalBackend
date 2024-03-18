# from django.db import models
# from django.contrib.auth.models import  AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.contrib.auth import get_user_model


# # Create your models here.
# class UserAccountManager(BaseUserManager):
#     def create_user(self, email, first_name,middle_name, last_name, user_name, role, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(email=email, first_name=first_name,middle_name=middle_name, last_name= last_name, user_name=user_name, role=role )
#         user.set_password(password)
#         user.save()
#         return user
# class Role(models.Model):
#     role_id = models.AutoField(primary_key=True)
#     role_name= models.CharField(max_length=30)
# class UserAccounts(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(max_length=254, unique=True)
#     first_name = models.CharField(max_length=30)
#     middle_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=100)
#     user_name = models.CharField(max_length=20,unique=True)
#     role = models.ForeignKey(Role,on_delete = models.CASCADE , related_name= 'role',null= False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
   
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['first_name','middle_name', 'last_name','user_name', 'role']
    
#     objects = UserAccountManager()

#     def get_full_name(self):
#         return self.first_name 
#     def get_short_name(self):
#         return self.first_name    
#     def __str__(self):
#         return self.email


# class Module(models.Model):
#     module_id= models.AutoField(primary_key= True)
#     module_name = models.CharField(max_length=30)
    
#     def str(self):
#         return self.module_name

        
# class Course(models.Model): 
#     featured_img =models.ImageField(upload_to='course_imga/',null=True, blank=True) 
#     course_name = models.CharField(max_length=100 ,null=True, blank=True)
#     title =models.TextField()
#     features =models.CharField(max_length =150) 
#     price = models.DecimalField(max_digits=10, decimal_places=2) 
#     module =models.ForeignKey(Module,null=False,  on_delete=models.CASCADE)
    
    
    
# class Instructor(models.Model):
#     GENDER_CHOICES = (
#       ('M', 'Male'),
#       ('F', 'Female'),
#       ('O', 'Prefer not to say'),
#     )
#     name = models.CharField(max_length=100)
#     gender = models.CharField(max_length = 1, choices = GENDER_CHOICES)
#     email = models.EmailField(unique = True)
#     phone_number = models.CharField(max_length = 15)
    
#     def __str__(self):
#         return self.name  
    
#     # user= models.ForeignKey(User,on_delete=models.CASCADE)
     
#     def __str__(self): 
#         return self.title
     

#     # class Meta: 
#     #     verbose_name_plural = '2. Course' 
#     #     # unique_together = (user, )
# class Video(models.Model):  
#     title = models.CharField(max_length = 100)
#     description = models.TextField()
#     video_file = models.FileField(upload_to="video/")
#     course = models.ForeignKey( Course ,on_delete =models.CASCADE , related_name = 'videos')
    
#     def __str__(self):
#         return self.title
    
# class WorkBook(models.Model):
#     title = models.CharField(max_length=100)
#     description =models.TextField()
#     pdf_file =models.FileField(upload_to='workbook/')  
#     course = models.ForeignKey(Course , on_delete=models.CASCADE ,related_name='workbooks')  
    
#     def __str__(self):
#         return self.title
    
# class Quiz(models.Model):
#     title = models.CharField(max_length=100)
#     questions = models.TextField()
#     course = models.ForeignKey(Course , on_delete = models.CASCADE , null = True)
    
#     def __str__(self):
#         return self.title

# class QuizQuestions(models.Model):
#     quiz = models.ForeignKey(Quiz , on_delete = models.CASCADE , null=True)
#     questions = models.CharField(max_length = 200)
#     ans1 = models.CharField(max_length = 200)
#     ans2 = models.CharField(max_length = 200)
#     ans3 = models.CharField(max_length = 200)
#     ans4 = models.CharField(max_length = 200)
#     right_ans = models.CharField(max_length = 200 )
#     add_time = models.CharField(max_length = 200)  
    
#     def __str__(self):
#         return self.questions

# class Enrollment(models.Model):
#     course = models.ForeignKey( Course , on_delete= models.CASCADE , null=True)
#     rating  = models.PositiveBigIntegerField(default = 0)
#     reviews = models.TextField(null =True, blank=True)
    