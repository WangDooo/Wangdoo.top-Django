from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.decorators.http import require_POST


from .models import ArticleColumn, ArticlePost
from .forms import ArticleColumnForm, ArticlePostForm

@login_required(login_url='/account/login/')
@csrf_exempt
def acrticle_column(request):
	if request.method == "GET":
		columns = ArticleColumn.objects.filter(user=request.user)
		column_form = ArticleColumnForm()
		return render(request, "article/column/article_column.html", {"columns":columns, "column_form":column_form})

	if request.method == "POST":
		column_name = request.POST['column']
		columns = ArticleColumn.objects.filter(user_id=request.user.id, column=column_name)
		if columns: # 判断栏目名称是否存在 这里有两个条件1.当前用户2.栏目名称
			return HttpResponse('2')
		else:
			ArticleColumn.objects.create(user=request.user, column=column_name)
			return HttpResponse('1')

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def rename_article_column(request):
	column_name = request.POST["column_name"]
	column_id = request.POST['column_id']
	try:
		line = ArticleColumn.objects.get(id=column_id) # 根据id查询到要修改的数据 建立实例对象
		line.column = column_name # 实现重新赋值
		line.save() # 保存到数据库
		return HttpResponse("1")
	except:
		return HttpResponse('0')

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_article_column(request):
	column_id = request.POST['column_id']
	try:
		line = ArticleColumn.objects.get(id=column_id)
		line.delete()
		return HttpResponse("1")
	except:
		return HttpResponse("2")

@login_required(login_url='/account/login/')
@csrf_exempt
def article_post(request):
	if request.method == "POST":
		article_post_form = ArticlePostForm(data=request.POST)
		if article_post_form.is_valid():
			cd = article_post_form.cleaned_data
			try:
				new_article = article_post_form.save(commit=False)
				new_article.author = request.user
				new_article.column = request.user.article_column.get(id=request.POST['column_id'])
				new_article.save()
				return HttpResponse("1")
			except:
				return HttpResponse("2")
		else:
			return HttpResponse("3")
	else:
		article_post_form = ArticlePostForm()
		acrticle_columns = request.user.article_column.all()
		return render(request, "article/column/article_post.html", {"article_post_form":article_post_form, "article_columns":acrticle_columns})

@login_required(login_url='/account/login/')
def article_list(request):
	articles = ArticlePost.objects.filter(author=request.user) # 筛选出用户的所有文章列表
	return render(request, "article/column/article_list.html", {"articles":articles})

@login_required(login_url='/account/login/')
def article_detail(request, id, slug):
	article = get_object_or_404(ArticlePost, id=id, slug=slug)
	return render(request, "article/column/article_detail.html", {"article":article})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_article(request):
	article_id = request.POST['article_id']
	try:
		article = ArticlePost.objects.get(id=article_id)
		article.delete()
		return HttpResponse("1")
	except:
		return HttpResponse("2")

@login_required(login_url='/account/login/')
@csrf_exempt
def redit_article(request, article_id):
	if request.method == "GET":
		article_columns = request.user.article_column.all()
		article = ArticlePost.objects.get(id=article_id)
		this_article_form = ArticlePostForm(initial={"title":article.title})
		this_article_column = article.column
		return render(request, "article/column/redit_article.html", {"article":article, "article_columns":article_columns, "this_article_column":this_article_column, "this_article_form":this_article_form})
