from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^brief_history/', views.history, name='history'),
    url(r'^our_activities/', views.activities, name='activities'),
    url(r'^board_and_committees/', views.board, name='board'),
    url(r'^theme_for_the_year/', views.theme, name='theme'),
    url(r'^beliefs_and_core_values/', views.beliefs, name='beliefs'),
]
