from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static  #Imported for images and css to work.

from . import views


urlpatterns = [
    url(r"^admin/", include(admin.site.urls)),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^quiz/(?P<quiz_id>[0-9]+)/question/(?P<question_id>[0-9]+)/$", views.quiz_view, name="quiz"),
    url(r"^quiz/(?P<quiz_id>[0-9]+)/results/$", views.result_view, name="result"),
]
