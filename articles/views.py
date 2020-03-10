from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articles_list(request):
    posts = Article.objects.all().order_by('date')
    context = {
        'posts': posts[:3], 'range': range(3)
    }
    return render(request, 'articles/articles_list.html', context)

def all_reviews(request):
	posts = Article.objects.all().order_by('date')
	context = { 'posts': posts }
	return render(request, 'articles/all_reviews.html', context)


def this_post(request, post_id):
	post = Article.objects.get(id=post_id)
	context = {
		'post': post,
	}
	return render(request, 'articles/this_post.html', context)

@login_required(login_url="/accountslogin")
def review(request):
	if request.method == 'POST':
		form = forms.CreateReview(request.POST)
		if form.is_valid():
			#wait, before saving, make an instance of 
			# what you're about to save (commit=False)
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('/articles')
	else:	
		form = forms.CreateReview()
		context = {'form': form}
		return render(request, 'articles/review.html', context)