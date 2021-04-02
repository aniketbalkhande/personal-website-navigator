from django.urls import path
from . import views
app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('site/', views.navigator, name='navigator'),
]
