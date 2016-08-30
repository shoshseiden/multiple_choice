from django.contrib import admin
from django.db.models import Q
from .models import Quiz, Question, Answer 


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    fields = ["quiz_name"]
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    fields =["quiz", "question_number", "question_point_value", "question_text",
        "correct_answer"]
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    fields = ["question", "answer_text"]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
