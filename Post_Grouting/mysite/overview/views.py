from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .models import Totalpile, Originalpile, Trypile
from kaisai.models import Kaisai
import json

@csrf_exempt
def overview(request):
	if request.method == "POST":
		pile_total = []
		pile_number = []
		# 获取的桩目前的信息
		trypile_name = []
		grout_name = []
		originalpile_name = []
		kaisaipile_name = []
		# 总桩信息共3004 填充这个字典
		piles_name = [] 
		# 用于生产piles_name
		for obj in Totalpile.objects.all():
			pile_total.append(obj.name)
			pile_number.append(obj.number)
		# 获取试桩列表
		trypile = Trypile.objects.values('name')
		ls_trypile = list(trypile)
		for each in ls_trypile:
			trypile_name.append(each['name'])
		# 获取原桩长列表
		originalpile = Originalpile.objects.values('name')
		ls_originalpile = list(originalpile)
		for each in ls_originalpile:
			originalpile_name.append(each['name'])
		# 获取开塞列表
		kaisaipile = Kaisai.objects.values('name')
		ls_kaisaipile= list(kaisaipile)
		for each in ls_kaisaipile:
			kaisaipile_name.append(each['name'])

		for i in range(len(pile_total)):
			for j in range(1,pile_number[i]+1):
				pile_name = pile_total[i]+'-'+str(j)
				if pile_name in trypile_name:
					piles_name.append({'name':pile_name,'value':'5'})
				elif pile_name in originalpile_name:
					piles_name.append({'name':pile_name,'value':'4'})
				elif pile_name in grout_name:
					piles_name.append({'name':pile_name,'value':'3'})
				elif pile_name in kaisaipile_name:
					piles_name.append({'name':pile_name,'value':'2'})
				else:
					piles_name.append({'name':pile_name,'value':'1'})

		data = json.dumps(piles_name)
		return HttpResponse(data, content_type="application/json")
	else:
		return render(request, "overview/overview.html")
