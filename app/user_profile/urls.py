# app/user_profile/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.user_profile.views import login_view, logout_view, register_view

app_name = 'user_profile'

urlpatterns = [

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),

]
