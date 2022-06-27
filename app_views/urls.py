from app_views import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='inicio'),
    path('about', views.about, name='sobremi'),
]