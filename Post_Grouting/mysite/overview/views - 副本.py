from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .models import Totalpile, Originalpile, Trypile

def overview(request):
	pile_total = []
	pile_number = []
	pile_1 = []
	pile_2 = []
	pile_3 = []
	pile_4 = []
	pile_5 = []
	pile_6 = []
	for obj in Totalpile.objects.all():
		pile_total.append(obj.name)
		pile_number.append(obj.number)
		pile_1.append(2)
		pile_2.append(2)
		pile_3.append(2)
		pile_4.append(2)
		pile_5.append(2)
		pile_6.append(2)
		
	piles = zip(pile_total, pile_number, pile_1, pile_2, pile_3, pile_4, pile_5, pile_6)
	return render(request, "overview/overview.html",{"piles":piles})
