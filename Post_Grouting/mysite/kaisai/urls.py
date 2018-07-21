from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'kaisai'
urlpatterns = [
	path('kaisai-post', views.kaisai_post, name='kaisai_post'),
	path('kaisai-list/', views.kaisai_list, name='kaisai_list'),
	path('kaisai-del/', views.kaisai_del, name="kaisai_del"),
	path('kaisai-detail/<slug>/', views.kaisai_detail, name="kaisai_detail"),
	path('kaisai-search/', views.kaisai_search, name="kaisai_search"),
	path('kaisai-show/<slug>/', views.kaisai_show, name="kaisai_show"),
]