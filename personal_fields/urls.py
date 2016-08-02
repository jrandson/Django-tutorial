from django.conf.urls import url
from django.shortcuts import render

from . import views

app_name = 'personal_fields'
urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^new_form/$',views.new_form,name='new_form'),
	url(r'^(?P<form_id>[0-9]+)/new_text_field/$',views.new_text_field,name='new_text_field'),
	url(r'^(?P<form_id>[0-9]+)/new_text_are/$',views.new_text_area,name='new_text_area'),
	url(r'^(?P<form_id>[0-9]+)/new_select_item/$',views.new_select_item,name='new_select_item'),
	url(r'^(?P<form_id>[0-9]+)/view_form/$',views.view_form,name='view_form'),
	#url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

]
