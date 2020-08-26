"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include,path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('homepage', views.index),
    path('db', views.reference_summary),
    path('new_input', views.new_input),
    path('search_engine', views.search_engine),
    path('login', views.login),
    path('manage', views.manage),
    
    
    ### OAuth2 setting
    #path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    ### using re_path
    #re_path(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    
    #path('detail/<int:id>', views.detail, name = 'detail-url'),
]
