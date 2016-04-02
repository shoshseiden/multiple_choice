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
