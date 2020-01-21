from django.contrib import admin
from .models import College, CollegeAdmin
# Register your models here.

admin.site.register(College, CollegeAdmin)
