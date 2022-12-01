""" Holds the URLs for the soul app """

from . import views
from django.urls import path
from django.views.generic import TemplateView

# urlpattern = [
#     path("", views.index, name= "index"),
# ]

urlpatterns = [
    path('', TemplateView.as_view(template_name = "home/index.html"), name='index'),
]