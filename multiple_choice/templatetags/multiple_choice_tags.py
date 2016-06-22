from __future__ import division

from django import template
from django.core.urlresolvers import reverse

from ..models import Question

register = template.Library()


@register.assignment_tag
def question_tags(quiz):
    pass
