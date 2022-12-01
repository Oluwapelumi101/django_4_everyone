""" All the views required for my cats applicatoin  """
from . import views
from django.urls import path
from django.views.generic import TemplateView, base

app_name = "cats"
urlpatterns = [
    path("", views.MainView.as_view(), name="index"),
    path("main/<int:pk>/update/", views.UpdateCat.as_view(), name="cat_update"),
    path("main/<int:pk>/delete/", views.DeleteCat.as_view(), name="cat_delete"),
    path("cat/create", views.CreateCat.as_view(), name="cat_create"),
    path("breed/create", views.CreateBreed.as_view(), name="breed_create"),
    path("breed/view", views.ListBreed.as_view(), name="breed_list"),
    path("breed/<int:pk>/update", views.UpdateBreed.as_view(), name="breed_update"),
    path("breed/<int:pk>/delete", views.DeleteBreed.as_view(), name="breed_delete"),
    # path("breeds", views.ListBreed.as_view(), name="breeds"),
]