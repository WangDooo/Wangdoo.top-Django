from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from .models import ArticleColumn
from .forms import ArticleColumnForm

@login_required(login_url='/account/login/')
@csrf_exempt
def acrticle_column(request):
	if request.method == "GET":
		columns = ArticleColumn.objects.filter(user=request.user)
		column_form = ArticleColumnForm()
		return render(request, "article/column/article_column.html", {"columns":columns, "column_form":column_form})

	if request.method == "POST":
		