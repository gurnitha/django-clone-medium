# config/urls.py

"""
https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # user_profile
    path('user/', include('app.user_profile.urls', namespace='user_profile')),

    # page
    path('', include('app.page.urls', namespace='page')),

    # admin
    path('admin/', admin.site.urls),
]
