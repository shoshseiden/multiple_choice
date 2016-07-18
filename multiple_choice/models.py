from django.db import models
from django.db.models import Max


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
"""
    @property
    def get_max_question(self, max_question):
        max_question = self.objects.all().aggregate(Max("question_number"))
        return max_question
"""
    def get_sequencing(self):
        total_question_numbers = self.objects.all().question_number
        current_question_number = self.objects.question_number
        question_number_list = []

        for current_question_number in total_question_numbers:
            if current_question_number:
                return question_number_list.append(current_question_number)
            else:
                return None 
