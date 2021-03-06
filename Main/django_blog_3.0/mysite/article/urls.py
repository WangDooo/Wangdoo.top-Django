from django.urls import path
from . import views, list_views

app_name = 'article'
urlpatterns = [
	path('article-column/', views.acrticle_column, name='article_column'),
	path('rename-column/', views.rename_article_column, name="rename_article_column"),
	path('del-column/', views.del_article_column, name="del_article_column"),
	path('article-post/', views.article_post, name="article_post"),
	path('article-list/', views.article_list, name="article_list"),
	path('article-detail/<int:id>/<slug>/', views.article_detail, name="article_detail"),
	path('del-article/', views.del_article, name="del_article"),
	path('redit-article/<int:article_id>/', views.redit_article, name="redit_article"),
	path('list-article-titles/', list_views.article_titles, name="article_titles"),
	path('list-article-detail/<int:id>/<slug>/', list_views.article_detail, name="list_article_detail"),
]