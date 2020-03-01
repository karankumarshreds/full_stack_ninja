from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('review', views.review, name='review'),
    path('<post_id>', views.this_post, name='this_post')
]
