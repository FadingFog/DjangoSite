from django.contrib import admin
from .models import Post, Tag, Hotel

admin.site.register(Post)
admin.site.register(Hotel)
admin.site.register(Tag)
