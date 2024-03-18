# from django.contrib import admin
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('module/', views.ModuleList.as_view()),
#     path('course/', views.CourseViewList.as_view(), name='course'),
#     path('viewUser/', views.UserCreateList.as_view(), name="user"),  
   
#     path('workbook/', views.WorkbookList.as_view()),
#     path('video/', views.VideoList.as_view()),
#     path('quiz/', views.QuizList.as_view()),
#     path('quizquestion/<int:quiz_id>', views.QuizQuestionList.as_view()),
# #     path('coursecontent/', views.CourseContentList.as_view()),
#     path('enrollments/', views.EnrollmentList.as_view()),
# #     path('reviews/', views.ReviewList.as_view()),
#     path('instructors/', views.InstructorList.as_view()),
# #     path('instructors/<int:pk>/', views.InstructorDetail.as_view()),
#     path("Role/" , views.RoleViewList.as_view())
# ]