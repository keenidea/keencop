from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^credit_union/', views.CreditView.as_view(), name='credit'),
    url(r'^school/', views.SchoolView.as_view(), name='school'),
    url(r'^clinic/', views.ClinicView.as_view(), name='clinic'),
]
