from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles

# Create your views here.
def articles_list(request):
    articles = Articles.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/articles_list.html', context)