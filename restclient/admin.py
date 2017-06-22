from django.contrib import admin

# Register your models here.
from restclient.models import University, Student

admin.site.register(University)
admin.site.register(Student)