from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
	right_code = '1234'
	if request.method == "POST":
		user_form = RegistrationForm(request.POST)
		userprofile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and userprofile_form.is_valid(): #:
			if userprofile_form.cleaned_data['invitation_code'] == right_code:
				new_user = user_form.save(commit=False)
				new_user.set_password(user_form.cleaned_data['password'])
				new_user.save()
				new_profile = userprofile_form.save(commit=False)
				new_profile.user = new_user
				new_profile.save()
				return HttpResponseRedirect(reverse('account:user_login'))
			else:
				return HttpResponse("抱歉，邀请码不对！")
		else:
			return HttpResponse("抱歉，注册中存在问题，若仍注册不成功，请联系管理员！")
	else:
		user_form = RegistrationForm()
		userprofile_form = UserProfileForm()
		return render(request, 'account/register.html', {"form": user_form, "profile":userprofile_form})


@login_required(login_url='/account/login/')
def myself(request):
	user = User.objects.get(username=request.user.username)
	userprofile = UserProfile.objects.get(user=user)
	return render(request, "account/myself.html", {"user":user, "userprofile":userprofile})

@login_required(login_url='/account/login/')
def myself_edit(request):
	user = User.objects.get(username=request.user.username)
	userprofile = UserProfile.objects.get(user=user)

	if request.method == "POST":
		user_form = UserForm(request.POST)
		userprofile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and userprofile_form.is_valid():
			user_cd = user_form.cleaned_data
			userprofile_cd = userprofile_form.cleaned_data
			user.email = user_cd['email']
			userprofile.realname = userprofile_cd['realname']
			userprofile.phone = userprofile_cd['phone']
			user.save()
			userprofile.save()
		return HttpResponseRedirect(reverse('account:my_information'))
	else: # 'GET'
		user_form = UserForm(instance=request.user)
		userprofile_form = UserProfileForm(initial={"realname":userprofile.realname, "phone":userprofile.phone, "invitation_code":userprofile.invitation_code})
		return render(request, "account/myself_edit.html", {"user_form":user_form, "userprofile_form":userprofile_form}) 
