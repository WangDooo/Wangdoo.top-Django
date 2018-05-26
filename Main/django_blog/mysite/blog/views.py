from django.shortcuts import render
from .models import BlogAritcles

def blog_title(request):
	blogs = BlogAritcles.objects.all()
	return render(request, "blog/titles.html", {"blogs":blogs})
