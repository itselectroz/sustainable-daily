from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .models.daily_data import DailyGoalStatus
from .models.survey import SurveyQuestion,SurveyChoice,Survey

# Register your models here.

admin.register(User, UserAdmin)
admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyChoice)
admin.site.register(User)
admin.site.register(DailyGoalStatus)
