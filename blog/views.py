from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from .models import Post, Hotel


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


class HotelListView(ListView):
    model = Hotel
    template_name = 'blog/hotel_list.html'


def index(request):
    return render(request, 'blog/index.html')
