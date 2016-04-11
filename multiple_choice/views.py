from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from .models import Quiz


def quiz(request, quiz_id):
    template_name = "multiple_choice_quiz.html"
    active_quiz = get_object_or_404(Quiz, pk=quiz_id)
    ctx = {'quiz': active_quiz}
    return render(request, template_name, ctx)

def question(request, quiz_id, question_id):
    p = get_object_or_404(Quiz, pk=quiz_id)
    try:
        active_question = p.question_set.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    else:
        return render(request, "multiple_choice_question.html", {'question': active_question})
