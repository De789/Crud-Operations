from django.contrib import admin

from .models import Employee, Student

# Register your models here.
admin.site.register(Employee)
admin.site.register(Student)


class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','rollno','city']