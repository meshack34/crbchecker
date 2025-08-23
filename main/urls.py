from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),

    path("report-purpose/", views.select_report_purpose, name="dashboard"),
    # path("generate-report/", views.generate_report, name="generate_report"),  # placeholder

    
]
# crb/settings.py