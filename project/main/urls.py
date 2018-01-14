from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/', views.index, name='index'),
    url(r'^home/$', views.home_page, name='home')
]