from django.urls import path
from . import views
app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('site/', views.navigator, name='navigator'),

    path('del/<int:id>/', views.deleteWebsite, name="deleteWebsite"),
    #path('site/update/<int:id>', views.updateWebsite, name="updateWebsite"),
]