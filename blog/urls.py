from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<str:slug>/', post_detail, name='post_detail'),
    path('tags/', tags_list, name='tag_list'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail'),
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
]
