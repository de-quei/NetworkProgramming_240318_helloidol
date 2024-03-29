"""
URL configuration for helloidol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mrsgreenapple/', include('mrsgreenapple.urls')),
    path('playground/', include('playground.urls')),
    # path('playground/hello/', playground.views.say_hello, name='playground_hello'), # 함수의 이름만 전달합니다 (소괄호 x)
    # path('playground/hello_html/', playground.views.say_hello_html, name='playground_hello_html'),
    path('admin/', admin.site.urls),
]
