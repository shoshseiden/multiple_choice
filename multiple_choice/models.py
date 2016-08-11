from django.db import models
from django.contrib.auth.models import User
# from django.db.models import Max


# User models
class Student(User):
    class Meta:
        proxy = True
        app_label = "auth"
        verbose_name = "Student Account"
        verbose_name_plural = "Student Accounts"


class Instructor(User):
    class Meta:
        proxy = True
        app_label = "auth"
        verbose_name = "Instructor Account"
        verbose_name_plural = "Instructor Accounts"


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=100)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz)
    question_number = models.IntegerField()
    question_text = models.TextField(null=True)
    correct_answer_choice = models.CharField(max_length=1) #A, B, C, or D
    correct_answer = models.CharField(max_length=25)
    incorrect_answer_1 = models.CharField(max_length=25)
    incorrect_answer_2 = models.CharField(max_length=25)
    incorrect_answer_3 = models.CharField(max_length=25)
    question_point_value = models.IntegerField()

    def __str__(self):
        return self.question_text
