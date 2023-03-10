"""pragmatic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accountapp.urls')), #accountapp안에 있는 url로 분기처리
    path('profiles/', include('profileapp.urls')), #profileapp안에 있는 url로 분기처리
    path('articles/', include('articleapp.urls')), #articleapp안에 있는 url로 분기처리
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # 설정을 해주어야 이미지가 보일수있게 처리가 가능하다
