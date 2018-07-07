from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
	path('article-column/', views.acrticle_column, name='article_column'),
]