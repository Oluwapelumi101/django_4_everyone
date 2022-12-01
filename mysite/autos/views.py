from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from autos.models import Auto, Make

from .forms.autos.forms import NameForm
from .forms.autos.make_form import MakeForm
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

# Implement by Dr.Chucks
# Class for the Make object
class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)
    
class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.all().count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}
        return render(request, 'autos/auto_list.html', ctx)

class MakeCreate(LoginRequiredMixin, View):
    template = 'autos/make_form.html'
    success_url = reverse_lazy('autos:all')

    def get(self, request):
        form = MakeForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request):
        form = MakeForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)
  
        form.save()
        return redirect(self.success_url)

class MakeUpdate(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_form.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'form': form}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(request.POST, instance=make)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)

class MakeDelete(LoginRequiredMixin, View):
    model = Make
    success_url = reverse_lazy('autos:all')
    template = 'autos/make_confirm_delete.html'

    def get(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        form = MakeForm(instance=make)
        ctx = {'make': make}
        return render(request, self.template, ctx)

    def post(self, request, pk):
        make = get_object_or_404(self.model, pk=pk)
        make.delete()
        return redirect(self.success_url)

# Class for the Auto fields
class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

# # Functional approach
# def index(request):
#     if request.user.is_authenticated:
#         makes = Make.objects.all()
#         # make_list = ", ".join([q.name for q in makes])
#         # return HttpResponse(make_list)
#         return render(request, "autos/make_list.html", {"make_list": makes})
#     else:
#         return HttpResponse("You need to sign in ")

# def my_form(request):
#     return render(request, "autos/forms.html")
#     # if request.get:
#     #     return HttpResponse(request)

# def get_name(request):
#     #procedure for handling a post reques
#     if request.method == "POST":
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.post)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/autos')            
#         # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'autos/forms.html', {'form': form})

# def update_make(request, pk):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             make = get_object_or_404(Make, pk=pk)
#             form = MakeForm(request.POST, instance=make)
#             form.save()
#             return HttpResponseRedirect('/autos')
#         else:
#             to_update = get_object_or_404(Make, pk=pk)
#             #print(Make.id)
#             form = MakeForm(instance=to_update)
#             return render(request, 'autos/forms.html', {'form': form})
#     else:
#         return HttpResponse("Please login")

""" to_update = get_object_or_404(Make, pk=pk)
Render a form with to_update filled in 
return HttpResponse(to_update) """

# Generic Class based Vies 
# class AutoCreate(LoginRequiredMixin, CreateView):
#     model = Auto
#     fields = "__all__"
#     succes_url = reverse_lazy("")
# CRUD Functions for Auto-Makes
# def create_make(request):
#     ...

# def delete_make(request):
#     ...

# def list_make(request):
#     ...
# CRUD Functions for Auto
# def create_auto(request):
#     ...

# def update_auto(request):
#     ...

# def delete_auto(request):
#     ...

# def list_auto(request):
    # ...

# class AboutView(LoginRequiredMixin, View):
#     def get(self, request):
#         autos = Auto.objects.all()
#         makes = Make.objects.all()
#         return render(request, "autos/make_list.html", {"make_list": makes})