from django.contrib import admin
from django.urls import path
from main_site import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_page, name='home')
]
