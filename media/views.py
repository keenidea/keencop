from django.shortcuts import render
from django.views import View


class NewsView(View):
    def get(self, request):
        return render(request, 'media/news.html', {})


class CalendarView(View):
    def get(self, request):
        return render(request, 'media/calendar.html', {})


class PressView(View):
    def get(self, request):
        return render(request, 'media/press.html', {})


class PhotoView(View):
    def get(self, request):
        return render(request, 'media/photo.html', {})


class SongsView(View):
    def get(self, request):
        return render(request, 'media/songs.html', {})


class VideoView(View):
    def get(self, request):
        return render(request, 'media/video.html', {})
