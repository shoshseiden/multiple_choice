from __future__ import division

from django import template
from django.core.urlresolvers import reverse

from ..models import Quiz, Question

register = template.Library()


@register.assignment_tag
def final_question(question_number):
    final_question = Question.question_number.get("-question_number")
    return {
              "final_question": final_question,
           }
