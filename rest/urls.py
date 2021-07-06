from django.urls import path
from . import views


pp_name = 'rest'
urlpatterns = [
    path(r'^$', views.IndexView.as_view(), name='index'),
    path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    path(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    path(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]