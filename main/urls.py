from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    
    path("services/", views.services_view, name="services"),
    path("solutions/", views.solutions_view, name="solutions"),
    path("about/", views.about_view, name="about"),
    path("contact/", views.contact_view, name="contact"),
]
# crb/settings.py