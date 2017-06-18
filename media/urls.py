from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^area_news/', views.NewsView.as_view(), name='news'),
    url(r'^area_calendar/', views.CalendarView.as_view(), name='calendar'),
    url(r'^press_release/', views.PressView.as_view(), name='press'),
    url(r'^photo_gallery/', views.PhotoView.as_view(), name='photo'),
    url(r'^pentecost_songs/', views.SongsView.as_view(), name='songs'),
    url(r'^video_gallery/', views.VideoView.as_view(), name='video'),
]
