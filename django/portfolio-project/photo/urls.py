#config/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')), # 이 때 URL 패턴을 '' 로 설정하면 photo 앱이 메인 페이지로 동작
]