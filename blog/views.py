from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import View, ListView
from .models import Post, Tag, Hotel
from .utils import ObjectDetailMixin


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})


class HotelListView(ListView):
    model = Hotel
    template_name = 'blog/hotel_list.html'
