from django.db import models

class QuizQuestion(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    a1 = models.CharField(max_length=255)
    a2 = models.CharField(max_length=255)
    a3 = models.CharField(max_length=255)
    a4 = models.CharField(max_length=255)

    CORRECT_CHOICES = [
        (1, 'a1'),
        (2, 'a2'),
        (3, 'a3'),
        (4, 'a4')
    ]
    
    correct_answer = models.IntegerField(choices=CORRECT_CHOICES)