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
    incorrect_answer_1 = models.CharField(max_length=25)
    incorrect_answer_2 = models.CharField(max_length=25)
    incorrect_answer_3 = models.CharField(max_length=25)
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
    """
    def get_total_score(self):

        point_value = self.question_point_value
        quiz_total = 0
        quiz_total += point_value
        return quiz_total

    def get_student_total(self, quiz_total):

        student_score = 0
        student_total += student_score
        student_percentage = student_total / quiz_total
        return student_percentage
    """
