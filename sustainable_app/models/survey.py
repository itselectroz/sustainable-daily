from django.db import models

class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    currentlyActive = models.BooleanField(default=False)
    survey_text = models.CharField(max_length=200)



class SurveyQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    Survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class SurveyChoice(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

