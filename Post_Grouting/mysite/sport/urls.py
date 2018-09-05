from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'sport'
urlpatterns = [
	path('', views.sport, name='sport'),
	path('sport-post', views.sport_post, name='sport_post'),
	path('del-card', views.del_card, name='del_card'),
	path('sport-list', views.sport_list, name='sport_list'),
	path('sport-list2', views.sport_list2, name='sport_list2'),
]