from django.db import models


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

    @property
    def final_question(self):
        return self.objects.last()
