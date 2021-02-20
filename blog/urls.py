from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail'),
    path('tags/', tags_list, name='tag_list'),
    path('tag/create', TagCreate.as_view(), name='tag_create'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail'),
    path('hotels/', HotelListView.as_view(), name='hotel_list'),
]
