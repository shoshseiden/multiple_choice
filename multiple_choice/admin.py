from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Quiz, Question, Student, Instructor


class InstructorAdmin(UserAdmin):
    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.filter(Q(is_staff=True)|Q(is_superuser=True))
        return qs


class StudentAdmin(InstructorAdmin):
    def queryset(self, request):
        qs = super(UserAdmin, self).queryset(request)
        qs = qs.exclude(Q(is_staff=True)|Q(is_superuser=True))
        return qs


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    fields = ["quiz_name"]
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Questions", {"fields": ["quiz", "question_number", "question_point_value",
         "question_text"]}),
        ("Answers", {"fields": ["correct_answer_choice",
         "correct_answer", "incorrect_answer_1", "incorrect_answer_2",
         "incorrect_answer_3"]}),
    ]



admin.site.unregister(User)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
