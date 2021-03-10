from django.utils import timezone
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Tag, Hotel
from .utils import *
from .forms import TagForm, PostForm


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_create.html'
    raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    redirect_url = 'index'
    raise_exception = True


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Tag
    redirect_url = 'tag_list'
    raise_exception = True


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})


# class HotelListView(ListView):
#     model = Hotel
#     template_name = 'blog/hotel_list.html'


def hotel_list(request):
    hotels = {'shit': 2, 'luxery': 50, 'kolyapidor': 1, 'meme': 100}
    return render(request, 'blog/hotel_list.html', {'hotels': hotels})
