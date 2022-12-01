from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Cat, Breed
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def index(request):
#     breeds = Breed.objects.all()
#     cats = Cat.objects.all()
#     return HttpResponse(breeds)

class MainView(LoginRequiredMixin, ListView):
    model = Cat
    template_name = "cats/all_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breed_count'] = Breed.objects.all().count()
        return context

class CreateBreed(LoginRequiredMixin, CreateView):
    model= Breed
    # fields = ["name"]
    fields = "__all__"
    template_name = "cats/temp_form.html"
    success_url = "/cats"

class ListBreed(LoginRequiredMixin, ListView):
    model = Breed
    print(model.objects.all())

class UpdateBreed(LoginRequiredMixin, UpdateView):
    model= Breed
    fields = ["name"]
    template_name = "cats/temp_form.html"
    success_url = "/cats/breed/view"

class DeleteBreed(LoginRequiredMixin, DeleteView):
    model = Breed
    # fields = ["name"]
    template_name = "cats/temp_confirm_delete.html"
    success_url = "/cats/breed/view"

    def model_name(self):
        return self.model._meta.verbose_name

class CreateCat(LoginRequiredMixin, CreateView):
    model= Cat
    # fields = ["name"]
    fields = "__all__"
    template_name = "cats/temp_form.html"
    success_url = "/cats"

class UpdateCat(LoginRequiredMixin, UpdateView):
    model= Cat
    fields = "__all__"
    template_name = "cats/temp_form.html"
    success_url = "/cats"

class DeleteCat(LoginRequiredMixin, DeleteView):
    model = Cat
    # fields = ["name"]
    template_name = "cats/temp_confirm_delete.html"
    success_url = "/cats"

    def model_name(self):
        return self.model._meta.verbose_name


