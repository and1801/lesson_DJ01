from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='news_home'),
path('create_news', views.create_news, name='add_news'),
]
