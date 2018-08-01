from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse


from .forms import GroutForm, ReportForm
from .models import Grout, Report, Surplus, Remaining
from overview.models import Piledetail
from slugify import slugify

from django.utils import timezone
import datetime

# 奖励函数
def reward(num):
	if num == 3:
		money = 50
	elif num == 4:
		money = 150
	elif num == 5:
		money = 250
	elif num == 6:
		money = 400
	elif num == 7:
		money = 550
	elif num == 8:
		money = 800
	else:
		money = 0
	return money

def update_surplus(user_id):
	amount_today = 0
	today =  datetime.datetime.now().strftime("%Y-%m-%d")
	yesterday = (datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
	surplus = Surplus.objects.filter(user=user_id)
	grout = Grout.objects.filter(user=user_id)
	grout_today = grout.filter(grout_date=today)
	for each in grout_today:
		amount_today = amount_today + each.amount
	if len(surplus) == 0:
		Surplus.objects.create(user=user_id)
	# Remaining表中，user的最新一次的 remain
	remains_yesterday = Remaining.objects.filter(user=user_id)
	if len(remains_yesterday) == 0:
		Remaining.objects.create(user=user_id,date=yesterday)
	remain_yesterday_ls = remains_yesterday.exclude(date=today)
	remain_yesterday = remain_yesterday_ls[len(remain_yesterday_ls)-1]
	# 选择Surplus中user的list- remaining_now
	remaining_now = Surplus.objects.filter(user=user_id)[0]
	# 当日总量
	remaining_now.amount_today = amount_today
	# 加上余量总共
	amount_sum = remain_yesterday.remain + amount_today
	remaining_now.amount_sum = amount_sum 
	# 折算根数
	conversion_number = amount_sum//8
	remaining_now.conversion_number = conversion_number
	# 奖励
	remaining_now.reward = reward(conversion_number)	
	# 余量
	remain_today = round(amount_sum%8,3)
	remaining_now.remaining = remain_today
	remaining_now.save()
	Remaining.objects.create(user=user_id,remain=remain_today)


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
				try:
					user_id = request.user
					update_surplus(user_id)
				except:
					return HttpResponse('<h1>更新余量出错</h1>')
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
		user_id = request.user
		update_surplus(user_id)
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
	date =  datetime.datetime.now().strftime("%Y-%m-%d")
	grouts = Grout.objects.filter(grout_date=date)
	reports = Report.objects.filter(date=date)
	
	person_ids = [] # 今日有上传的id

	for obj in grouts:
		if obj.user not in person_ids:
			person_ids.append(obj.user)

	person_grouts = Surplus.objects.filter(user__in=person_ids)

	return render(request, 'grout/grout_show.html', {"date":date, "grouts":grouts, "reports":reports, "person_grouts":person_grouts})


def grout_difference(request):
	differences = []
	grouts = Grout.objects.all()
	piles = Piledetail.objects.all()
	for grout in grouts:
		if grout.amount==0:
			differences.append({"name":grout.name,"design_amount":'此桩已压',"fact_amount":'缺压浆表'})
		else:
			for pile in piles:
				if (grout.name==pile.name) and (grout.amount+0.21<pile.grout_amount):
					difference = round(pile.grout_amount - grout.amount,2)
					differences.append({"name":grout.name,"design_amount":pile.grout_amount,"fact_amount":grout.amount,"difference":difference})

	return render(request, 'grout/grout_difference.html', {"differences":differences})