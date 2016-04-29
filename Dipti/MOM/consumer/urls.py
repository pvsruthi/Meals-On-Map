from django.conf.urls import url

from . import views

urlpatterns = [
    
    #ex: /consumer/
    url(r'^$', views.index, name='index'),

    #ex: /consumer/results/zip/94608/date/2016-04-12/   
    ################# FIX the RE for Date part later. ###############################
    url(r'^results/zip/(?P<query_zip>[0-9]+)/date/(?P<query_date>.*)/$', views.ResultsView.as_view(), name='results_list'),
]


'''
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
'''
