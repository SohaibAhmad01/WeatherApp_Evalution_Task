from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('checkweather', views.getweather, name="checkweather"),
    path('add_to_fav', views.add_favorate, name="add_to_fav"),
]

