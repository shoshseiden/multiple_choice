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
