from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from .models import Post, Tag, Hotel


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    return render(request, 'blog/tag_detail.html', {'tag': tag})


class HotelListView(ListView):
    model = Hotel
    template_name = 'blog/hotel_list.html'
