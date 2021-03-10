from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj, 'admin_obj': obj})


class ObjectCreateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, {'form': form, 'name': self.model.__name__.lower()})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, {'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = 'blog/obj_update.html'

    def get(self, request, slug):
        obj = self.model.objects.get(slug__exact=slug)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, {'form': bound_form, 'obj': obj, 'name': self.model.__name__.lower()})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__exact=slug)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, {'form': bound_form,  self.model.__name__.lower(): obj})


class ObjectDeleteMixin:
    model = None
    template = 'blog/obj_delete.html'
    redirect_url = None

    def get(self, request, slug):
        obj = self.model.objects.get(slug__exact=slug)
        return render(request, self.template, {'obj': obj, 'name': self.model.__name__.lower()})

    def post(self, request, slug):
        obj = self.model.objects.get(slug__exact=slug)
        obj.delete()
        return redirect(reverse(self.redirect_url))
