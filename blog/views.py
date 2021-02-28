from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import View, ListView
from .models import Post, Tag, Hotel
from .utils import *
from .forms import TagForm, PostForm


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})


class HotelListView(ListView):
    model = Hotel
    template_name = 'blog/hotel_list.html'
