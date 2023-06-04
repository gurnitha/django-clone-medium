# app/page/views.py

# Django and third parties modules
from django.shortcuts import render

# Locals

# Create your views here.

def home_view(request):
	return render(request, 'page/home_page.html')