from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static  #Imported for images and css to work.

from . import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", TemplateView.as_view(template_name="homepage.html"), name="home"),
    url(r"^quiz/(?P<quiz_id>[0-9]+)/$", views.quiz, name="quiz"),
    url(r"^quiz/(?P<quiz_id>[0-9]+)/question/(?P<question_id>[0-9]+)/$", views.question, name="question"),
    #url(r"^quiz/(?P<question_id>[0-9]+)/m_A/$", views.multiple_a, name="multiple_a"),
    #url(r"^quiz/(?P<question_id>[0-9]+)/m_B/$", views.multiple_a, name="multiple_b"),
    #url(r"^quiz/(?P<question_id>[0-9]+)/m_C/$", views.multiple_a, name="multiple_c"),
    #url(r"^quiz/(?P<question_id>[0-9]+)/m_D/$", views.multiple_a, name="multiple_d"),
    url(r"^answer/$", views.multiple_a, name="multiple_a")
]
