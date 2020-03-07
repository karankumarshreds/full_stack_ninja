from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm as uc_form
from django.contrib.auth.forms import AuthenticationForm as a_form
from django.contrib.auth import login, logout

# Create your views here.
def register(request):

	if request.method == 'POST':
		form = uc_form(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/articles')
	else:		
		form = uc_form()
	context = {'form': form}
	return render(request, 'accounts/register.html', context)

def log_in(request):

	if request.method == 'POST':
		form = a_form(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('/articles')
		else:
			return redirect('/accountslogin')
	else:
		form = a_form()
	context = {'form': form}
	return render(request, 'accounts/login.html', context)

def log_out(request):
	
	if request.method == 'POST':
		logout(request)
		return redirect('/articles')



