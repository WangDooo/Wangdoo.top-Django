from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'overview'
urlpatterns = [
	path('', views.overview, name='overview'),
	path('pile-detail/', views.pile_detail, name='pile_detail'),
]