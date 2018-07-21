from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .forms import KaisaiForm
from .models import Kaisai

import os

@login_required(login_url='/account/login/')
@csrf_exempt
def kaisai_post(request):
	if request.method == "POST":
		form = KaisaiForm(request.POST, request.FILES)
		if form.is_valid():
			try:
				new_item = form.save(commit=False)
				new_item.user = request.user
				new_item.name = new_item.name.upper()
				new_item.save()
				return HttpResponseRedirect(reverse('kaisai:kaisai_post'))
			except:
				return HttpResponse('上传中有问题！')
		else:
			return HttpResponse('1.上传的桩号已存在！或 2.上传文件非图片格式！')
	else:
		kaisai_form = KaisaiForm()
		return render(request, 'kaisai/kaisai_post.html', {"kaisai_form": kaisai_form})


@login_required(login_url='/account/login/')
def kaisai_list(request):
	images = Kaisai.objects.filter(user=request.user)
	return render(request, 'kaisai/kaisai_list.html', {"images":images})


@login_required(login_url='/account/login/')
def kaisai_detail(request, slug):
	kaisai = get_object_or_404(Kaisai, slug=slug)
	return render(request, "kaisai/kaisai_detail.html", {"kaisai":kaisai})


@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def kaisai_del(request):
	image_id = request.POST['kaisai_id']
	try:
		image = Kaisai.objects.get(id=image_id)
		fname = image.image.path
		if os.path.isfile(fname):
			os.remove(fname)
		image.delete()
		return HttpResponse("1")
	except:
		return HttpResponse("2")

@csrf_exempt
def kaisai_search(request):
	if request.method == "POST":
		name = request.POST['name'].upper()
		try:
			kaisai = Kaisai.objects.filter(name=name)[0]
			if kaisai:
				return HttpResponseRedirect(reverse('kaisai:kaisai_show',args=[kaisai.slug,]))
			else:
				return HttpResponse("没有此桩开塞表，请注意输入格式！")
		except:
			return HttpResponse("没有此桩开塞表，请注意输入格式！")
	else:
		return render(request, "kaisai/kaisai_search.html")


def kaisai_show(request, slug):
	kaisai = get_object_or_404(Kaisai, slug=slug)
	return render(request, "kaisai/kaisai_show.html", {"kaisai":kaisai})