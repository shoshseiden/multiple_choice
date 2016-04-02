from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django import template
from django.template.loader import get_template
from django.template import RequestContext, loader
from django.views import generic

from .models import Quiz, Question, Answer


class QuizView(generic.TemplateView):

    model = Quiz
    template_name = "multiple_choice_quiz.html"


def question(request, question_id):
    template_name = "multiple_choice_question.html"
    active_question = get_object_or_404(Question, pk=question_id)
    ctx = {'question': active_question}
    return render(request, template_name, ctx)
