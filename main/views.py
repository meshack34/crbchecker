from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

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


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect("login")  # Replace with your login url
    else:
        form = RegisterForm()
    return render(request, "main/register.html", {"form": form})
