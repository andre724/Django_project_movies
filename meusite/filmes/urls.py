from django.urls import path

from . import views

urlpatterns = [
    path("<int:id>", views.filme, name="filme"),
    path('', views.index, name='index'),
]