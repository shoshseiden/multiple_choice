from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):

    quiz_name = models.CharField(max_length=100)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):

    quiz = models.ForeignKey(Quiz)
    question_number = models.IntegerField()
    question_text = models.TextField(null=True)
    correct_answer = models.CharField(max_length=25)
    # incorrect_answer_1 = models.CharField(max_length=25)
    # incorrect_answer_2 = models.CharField(max_length=25)
    # incorrect_answer_3 = models.CharField(max_length=25)
    question_point_value = models.IntegerField()

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

    @property
    def get_answer_list(self):

        answer_list = [self.correct_answer, self.incorrect_answer_1, self.incorrect_answer_2,
            self.incorrect_answer_3]
        return answer_list

class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_input = models.CharField(max_length=25)

    def __str__(self):
        return self.answer_input
