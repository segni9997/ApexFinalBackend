from django.contrib import admin
from .import models

# # Register your models here.
admin.site.register(models.Module)
admin.site.register(models.Course)
# admin.site.register(models.CourseContent)

admin.site.register(models.WorkBook)
admin.site.register(models.Video)
admin.site.register(models.Quiz)
admin.site.register(models.QuizQuestions)
admin.site.register(models.Instructor)
admin.site.register(models.Enrollment)
admin.site.register(models.Role)