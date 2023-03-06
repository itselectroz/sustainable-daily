from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .models.survey import Question,Choice

# Register your models here.

admin.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Choice)