from django.urls import path
from . import views
from blog.views import HotelListView

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('hotels/', HotelListView.as_view()),
]
