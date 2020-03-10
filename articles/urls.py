from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('review', views.review, name='review'),
    path('all_reviews', views.all_reviews, name='all_reviews'),
    path('<post_id>', views.this_post, name='this_post')
]
