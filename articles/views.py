from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles_list(request):
    posts = Article.objects.all().order_by('date')
    context = {
        'posts': posts,
    }
    return render(request, 'articles/articles_list.html', context)

def this_post(request, post_id):
	post = Article.objects.get(id=post_id)
	context = {
		'post': post,
	}
	return render(request, 'articles/this_post.html', context)

@login_required(login_url="/accountslogin")
def review(request):
	return render(request, 'articles/review.html', {})