from django.shortcuts import render, get_object_or_404
from .models import Post, Tag


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj})
