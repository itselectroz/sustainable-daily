from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User, Goal, DailyData, DailyGoalStatus,
    SurveyQuestion, SurveyChoice, Survey
)

# Register your models here.
admin.register(User, UserAdmin)
admin.site.register(Goal)
admin.site.register(DailyData)
admin.site.register(DailyGoalStatus)
admin.site.register(Survey)
admin.site.register(SurveyQuestion)
admin.site.register(SurveyChoice)
admin.site.register(User)
