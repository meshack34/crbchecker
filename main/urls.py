from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("register/", views.register, name="register"),
]
# crb/settings.py