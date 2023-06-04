# app/user_profile/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals

# Create your views here.

def login_view(request):
	return render(request, 'user_profile/login.html')
