# config/urls.py

"""
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # page
    path('', include('app.page.urls', namespace='page')),

    # admin
    path('admin/', admin.site.urls),
]
