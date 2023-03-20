from django.db import models
from . import Goal


class Survey(models.Model):
    """
    Represents a survey object that will be loaded by the survey page which will load the questions attatched to the loaded survey object
    """
    id = models.AutoField(primary_key=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    survey_text = models.CharField(max_length=200)


class SurveyQuestion(models.Model):
    """
    Represents a question in a survey that can have up to 4 options (otherwise can cause formatting issues on smaller screens) 
    """
    id = models.AutoField(primary_key=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class SurveyChoice(models.Model):
    """
    Represents a choice for a question in a survey and how many votes that choice has
    """
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(SurveyQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
