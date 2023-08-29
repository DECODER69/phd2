from django.urls import path
from . import views
from django.conf.urls import static
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from django.urls import include, re_path
app_name = 'activities'

urlpatterns = [
    path('', views.pcg, name='pcg'),
    path('list', views.list, name='list'),
    path('profile', views.profile, name='profile'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)