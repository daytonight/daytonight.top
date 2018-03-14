from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^css/', views.index, name='index'),
    url(r'^home/$', views.home_page, name='home'),
    url(r'', views.home_page, name='home'),
]