from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'grout'
urlpatterns = [
	path('grout-post', views.grout_post, name='grout_post'),
	path('grout-list/', views.grout_list, name='grout_list'),
	path('grout-del/', views.grout_del, name="grout_del"),
	path('grout-edit/<str:grout_id>/', views.grout_edit, name="grout_edit"),
]