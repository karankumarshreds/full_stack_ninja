from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def articles(request):
    return render(request, 'articles/articles_list.html', {})