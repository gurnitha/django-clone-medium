# app/page/urls.py

# Django and third parties modules
from django.urls import path

# Locals
from app.page.views import home_view

app_name = 'page'

urlpatterns = [

    path('', home_view, name='home'),

]
