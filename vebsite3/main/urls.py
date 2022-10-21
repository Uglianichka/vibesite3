from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name = 'glav'),
    path('home', views.index_1, name = 'home'),
    path('about-as', views.about, name = 'about')
]