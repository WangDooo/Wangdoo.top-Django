from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Punchcard

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
		return render(request, 'sport/sport_post.html')


def sport_list2(request):
	sports = Punchcard.objects.filter(user=request.user)
	return render(request, 'sport/sport_list2.html', {"sports":sports})

def sport_list(request):
	return render(request, 'sport/sport_list.html')