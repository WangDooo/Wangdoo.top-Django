from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'grout'
urlpatterns = [
	path('grout-post', views.grout_post, name='grout_post'),
	path('grout-list/', views.grout_list, name='grout_list'),
	path('grout-del/', views.grout_del, name="grout_del"),
	path('grout-edit/<str:grout_id>/', views.grout_edit, name="grout_edit"),
	path('report-post', views.report_post, name='report_post'),
	path('report-list', views.report_list, name='report_list'),
	path('report-del/', views.report_del, name="report_del"),
	path('grout-show/', views.grout_show, name="grout_show"),
	path('grout-difference/', views.grout_difference, name="grout_difference"),
]