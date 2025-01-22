from . import views
from django.urls import path
urlpatterns = [
    path('', views.data),
    path('test', views.test)
]
