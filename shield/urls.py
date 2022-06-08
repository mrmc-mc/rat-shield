from django.urls import path,include
from . import views


app="rat"
urlpatterns = [
    path('', views.Index.as_view(),name="index"),
]