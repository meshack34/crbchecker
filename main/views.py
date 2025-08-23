from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")
        else:
            print(form.errors)  # 👈 Debug
    else:
        form = RegisterForm()
    return render(request, "main/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  # change to your homepage
        else:
            messages.error(request, "Invalid email or password")
    return render(request, "main/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def home_view(request):
    testimonials = [
        ('David Omondi', 'IT Consultant', 'Regular credit monitoring has helped me maintain a good credit score. The mobile app makes it convenient to check my status anytime.'),
        ('Bill Musyoka', 'Verified Customer', 'I have been using CRB Check for a few months now and I am very happy with the service. The app is easy to use and the customer support is great.'),
        ('Wilton Kamau', 'Business Consultant', 'The interface is clean and user-friendly, which makes it easy to get things done quickly. Plus, the support team is responsive and genuinely helpful.'),
        ('Evans Koech', 'Teacher', 'The service has been working incredibly well especially when applying for loans. Great app, easy to use, and excellent customer support.'),
        ('Brian Kimani', 'Verified Customer', 'The platform is intuitive, and the customer support has been excellent.'),
        ('Jane Kairitu', 'Farmer', 'The interface is clean and user-friendly. The support team is responsive and genuinely helpful.'),
    ]
    return render(request, 'main/home.html', {
        'year': datetime.now().year,
        'testimonials': testimonials
    })



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReportPurposeForm

@login_required
def select_report_purpose(request):
    if request.method == "POST":
        form = ReportPurposeForm(request.POST)
        if form.is_valid():
            purpose = form.save(commit=False)
            purpose.user = request.user
            purpose.save()
            # redirect to next step (report generation page)
            return redirect("report_purpose")
    else:
        form = ReportPurposeForm()
    return render(request, "main/report_purpose.html", {"form": form})
