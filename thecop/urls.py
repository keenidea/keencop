"""thecop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('index.urls', namespace='index', app_name='index')),
    url(r'^about_us/', include('about.urls', namespace='about', app_name='abouts')),
    url(r'^ministries/', include('ministries.urls', namespace='ministries', app_name='ministries')),
    url(r'^contact/', include('contact.urls', namespace='contact', app_name='contact')),
    url(r'^leadership/', include('leadership.urls', namespace='leadership', app_name='leadership')),
    url(r'^area_media/', include('media.urls', namespace='media', app_name='media')),
    url(r'^social_welfare/', include('welfare.urls', namespace='welfare', app_name='welfare')),
]
