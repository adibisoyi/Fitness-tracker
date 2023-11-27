from django.contrib import admin

# Register your models here.

from .models import User,User_matrix,Exercise_details

admin.site.register(User)
admin.site.register(User_matrix)
admin.site.register(Exercise_details)