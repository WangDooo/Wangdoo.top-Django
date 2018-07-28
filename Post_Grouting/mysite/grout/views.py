from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .forms import GroutForm, ReportForm
from .models import Grout, Report
from slugify import slugify

from django.utils import timezone


@login_required(login_url='/account/login/')
@csrf_exempt
def grout_post(request):
	if request.method == "POST":
		form = GroutForm(request.POST)
		if form.is_valid():
			try:
				new_item = form.save(commit=False)
				new_item.user = request.user
				new_item.name = new_item.name.upper() 
				new_item.save()
				return HttpResponseRedirect(reverse('grout:grout_list'))
			except:
				return HttpResponse('<h1>上传中有问题！</h1>')
		else:
			return HttpResponse('<h1>上传失败，可能原因：1.上传的桩号已存在！2.日期格式错误</h1>')
	else:
		grout_form = GroutForm()
		return render(request, 'grout/grout_post.html', {"grout_form": grout_form})


@login_required(login_url='/account/login/')
def grout_list(request):
	grouts = Grout.objects.filter(user=request.user)
	return render(request, 'grout/grout_list.html', {"grouts":grouts})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def grout_del(request):
	grout_id = request.POST['grout_id']
	try:
		grout = Grout.objects.get(id=grout_id)
		grout.delete()
		return HttpResponse("1")
	except:
		return HttpResponse("2")

@login_required(login_url='/account/login/')
@csrf_exempt
def grout_edit(request, grout_id):
	grout = Grout.objects.get(id=grout_id)
	if request.method == "POST":
		try:
			form_name = request.POST['name'].upper()
			grout.name = form_name 
			grout.slug = slugify(form_name)
			grout.amount = request.POST['amount']
			grout.remark = request.POST['remark']
			grout.grout_date = request.POST['grout_date']
			grout.save()
			return HttpResponseRedirect(reverse('grout:grout_list'))
		except:
			return HttpResponse("修改失败！1.可能已经存在此桩信息，请先删除原纪录！2.时间格式错误")
	else: 
		grout_form = GroutForm(initial={"name":grout.name, "amount":grout.amount, "remark":grout.remark, "grout_date":grout.grout_date})
		return render(request, "grout/grout_edit.html", {"grout_form":grout_form,"grout":grout}) 

@login_required(login_url='/account/login/')
@csrf_exempt
def report_post(request):
	if request.method == "POST":
		form = ReportForm(request.POST)
		if form.is_valid():
			try:
				new_item = form.save(commit=False)
				new_item.user = request.user
				new_item.save()
				return HttpResponseRedirect(reverse('grout:report_post'))
			except:
				return HttpResponse('<h1>上传中有问题！</h1>')
		else:
			return HttpResponse('<h1>上传失败!</h1>')
	else:
		report_form = ReportForm()
		return render(request, 'grout/report_post.html', {"report_form": report_form})

@login_required(login_url='/account/login/')
def report_list(request):
	reports = Report.objects.filter(user=request.user)
	return render(request, 'grout/report_list.html', {"reports":reports})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def report_del(request):
	report_id = request.POST['report_id']
	try:
		report = Report.objects.get(id=report_id)
		report.delete()
		return HttpResponse("1")
	except:
		return HttpResponse("2")

def grout_show(request):
	date = timezone.now()
	return render(request, 'grout/grout_show.html', {"date":date})