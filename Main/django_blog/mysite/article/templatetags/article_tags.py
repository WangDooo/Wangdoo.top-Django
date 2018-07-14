from django import template # 只有注册过的标签，系统才能识别，这是固定写法

register = template.Library()

from django.utils.safestring import mark_safe

from article.models import ArticlePost

import markdown

@register.simple_tag
def total_articles():
	return ArticlePost.objects.count()

@register.simple_tag
def author_total_articles(user):
	return user.article.count()

@register.inclusion_tag('article/list/latest_articles.html')
def lasted_articles(n=5):
	latest_article = ArticlePost.objects.order_by("-created")[:n]
	return {"latest_articles":latest_article}

from django.db.models import Count

@register.simple_tag
def most_commented_articles(n=3):
	return list(ArticlePost.objects.annotate(total_comments=Count("comments")).order_by("-total_comments")[:n])

@register.filter(name='markdown')
def markdown_filter(text):
	return mark_safe(markdown.markdown(text))