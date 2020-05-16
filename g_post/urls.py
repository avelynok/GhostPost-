from django.urls import path
from g_post import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('add_post/', views.add_post, name='add_post'),
    path('upVote/<int:post_id>/', views.upVote, name='upVote'),
    path('downVote/<int:post_id>/', views.downVote, name='downVote'),
    path('high_to_low/', views.high_to_low, name='high_to_low'),
    path('low_to_high/', views.low_to_high, name='low_to_high'),
    path('roast/', views.roast, name='roast'),
    path('boast/', views.boast, name='boast')
]