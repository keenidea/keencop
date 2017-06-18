from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^evangelism_ministry/', views.evangelism, name='evangelism'),
    url(r'^men_ministry/', views.men, name='men'),
    url(r'^women_ministry/', views.women, name='women'),
    url(r'^youth_ministry/', views.youth, name='youth'),
    url(r'^children_ministry/', views.children, name='children'),
]
