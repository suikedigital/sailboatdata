from django.contrib import admin
from django.urls import path, include
from boats import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL for the homepage
    path('boats/', include('boats.urls')),  # Ensure 'boats/' has a trailing slash
]