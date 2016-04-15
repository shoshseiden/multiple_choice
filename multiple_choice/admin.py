from django.contrib import admin
from .models import Quiz, Question


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    fields = ["quiz_name"]
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Questions", {"fields": ["quiz", "question_number", "question_text"]}),
        ("Answers", {"fields": ["correct_answer_letter",
         "correct_answer", "incorrect_answer_1", "incorrect_answer_2",
         "incorrect_answer_3"]}),
    ]




admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
