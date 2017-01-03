from django.db import models
from django.contrib.auth.models import User

import numpy as np


class Quiz(models.Model):

    quiz_name = models.CharField(max_length=100)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):

    quiz = models.ForeignKey(Quiz)
    question_number = models.IntegerField()
    question_text = models.TextField(null=True)
    correct_answer = models.CharField(max_length=25)
    question_point_value = models.IntegerField()

    #@@@ Set up correct answer so that it will get added into the score.

    def total_quiz_score(self):
        total_score = map(lambda: x.answer_text, self.answer_set.all())

    def __str__(self):
        return self.question_text

    @property
    def next_question(self):

        qs = self.quiz.question_set.filter(
            question_number__gt=self.question_number
        ).order_by("question_number")[:1]
        try:
            return qs.get()
        except Question.DoesNotExist:
            return None

    # @property
    # def get_total_quiz_score(self):
    #
    #     correct_answer = self.correct_answer
    #     question_point_value = self.question_point_value
    #     quiz_total = 0
    #
    #     quiz_total += question_point_value
    #     return quiz_total



class Answer(models.Model):

    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=25)

    def __str__(self):
        return self.answer_text

        @property
        def get_answer_list(self):

            answer_list = []
            answer_list.append(self.answer_text)
            return answer_list
