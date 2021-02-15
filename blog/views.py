from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from .models import Post, Hotel


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


class HotelListView(ListView):
    model = Hotel
    template_name = 'blog/hotel_list.html'


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})
