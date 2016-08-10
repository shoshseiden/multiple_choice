from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from .forms import StudentLoginForm, InstructorLoginForm
from .models import Quiz, Question


def quiz_view(request, quiz_id, question_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    question = get_object_or_404(quiz.question_set.all(), pk=question_id)
    if request.method == "POST":
        if request.POST["answer"] == question.correct_answer:
            next_question = question.next_question
            if next_question is None:
                return redirect("result", quiz_id=quiz.id)
            else:
                return redirect("quiz", quiz_id=quiz.id, question_id=next_question.id)
    ctx = {
        "question": question,
        "quiz": quiz
    }
    return render(request, "multiple_choice_quiz.html", ctx)


def result_view(request, quiz_id):
    p = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, "results.html", {'quiz': p})

def login_view(request):
    if request.method=="POST":
        student_form = StudentLoginForm(request.POST)
        instructor_form = InstructorLoginForm(request.POST)
        if student_form.is_valid():
            return redirect("home")
        if instructor_form.is_valid():
            return redirect("home")
    else:
        student_form = StudentLoginForm()
        instructor_form = InstructorLoginForm()
    return render(request, "login.html", {"student_form": student_form, "instructor_form": instructor_form})
