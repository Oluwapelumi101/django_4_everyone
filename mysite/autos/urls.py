""" Holds the URLs for the autos app """

from . import views
from django.urls import path
from django.views.generic import TemplateView, base

app_name = "autos"
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),


    # path("forms", views.get_name, name="form"),
    # # path("make_update/<int:pk>", views.update_make, name="make_update"),
    # # path("make_delete/<int:pk>", views.delete_make, name="make_delete"),
    # path('about/', views.AboutView.as_view()),
    # path("test", views.my_form, name="test_form"), 
    # path("temp", TemplateView.as_view(), name="template"),
    # path("", views.index, name= "index"),
]

""" 
Experimental URLS
path('about/', views.AboutView.as_view()),
path("test", views.my_form, name="test_form"), 
path("temp", TemplateView.as_view(), name="template"),
path("", views.index, name= "index"),
"""