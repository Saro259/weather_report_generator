from django.contrib import admin
from django.urls import path
from weather_dashboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weatherReport/', views.weather_page)
]
