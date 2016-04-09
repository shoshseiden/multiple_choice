from django.contrib import admin
from .models import Quiz, Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1

class QuizAdmin(admin.ModelAdmin):
    fields = ["quiz_name"]


class QuestionAdmin(admin.ModelAdmin):
    fields = ["quiz", "question_number", "question_text"]
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    fields = ["question", "correct_answer", "incorrect_answer_1", "incorrect_answer_2",
                "incorrect_answer_3"]




admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
