from . import views
from django.urls import path
urlpatterns = [
    path('', views.index, name='home'),
    path('newnewnew', views.new, name='page2'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]
