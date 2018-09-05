from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from .models import Punchcard
import datetime

def sport(request):
	return render(request, 'sport/sport.html')

@login_required(login_url='/account/login/')
@csrf_exempt
def sport_post(request):
	if request.method == "POST":
		try:
			new_item = Punchcard()
			new_item.sport = request.POST['sport']
			new_item.remark = request.POST['remark']
			new_item.user = request.user
			new_item.save()
		except:
			return HttpResponse('<h1>上传中有问题！</h1>')
		return HttpResponseRedirect(reverse('sport:sport_list2'))
	else:
		today = datetime.datetime.now().strftime("%Y-%m-%d")
		sports = Punchcard.objects.filter(user=request.user)
		sport_today = sports.filter(publish_date=today)
		if len(sport_today):
			today_card = '1'
		else:
			today_card = '2'
			sport_today = ['1']
		return render(request, 'sport/sport_post.html', {"sport_today":sport_today[0],"today_card":today_card})

@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def del_card(request):
	card_id = request.POST['card_id']
	try:
		card = Punchcard.objects.get(id=card_id)
		card.delete()
		return HttpResponse("1")
	except:
		return HttpResponse("2")


@login_required(login_url='/account/login/')
def sport_list2(request):
	sports = Punchcard.objects.filter(user=request.user)
	return render(request, 'sport/sport_list2.html', {"sports":sports})



@login_required(login_url='/account/login/')
def sport_list(request):
	return render(request, 'sport/sport_list.html')

