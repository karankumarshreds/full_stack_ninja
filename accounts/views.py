from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm as uc_form

# Create your views here.
def register(request):

	if request.method == 'POST':
		form = uc_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/articles')
	else:		
		form = uc_form()
		context = {
			'form': form
		}
	return render(request, 'accounts/register.html', context)
